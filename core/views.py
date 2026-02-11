import json
import os
import importlib.util
from datetime import datetime

import cv2
import numpy as np
from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import AlarmHistory, Anomaly, User
from .rendering import render_template
from .session_auth import admin_required, get_current_user, login_required


_ML_MODEL = None


def _get_ml_model():
    global _ML_MODEL
    if _ML_MODEL is not None:
        return _ML_MODEL

    model_py = os.path.join(settings.BASE_DIR, 'app', 'model.py')
    spec = importlib.util.spec_from_file_location('crowdguard_ml_model', model_py)
    if spec is None or spec.loader is None:
        _ML_MODEL = None
        return _ML_MODEL

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _ML_MODEL = getattr(module, 'model', None)
    return _ML_MODEL


def home(request: HttpRequest) -> HttpResponse:
    return render_template(request, 'home.html')


@csrf_exempt
def login_view(request: HttpRequest) -> HttpResponse:
    current_user = get_current_user(request)
    if current_user.is_authenticated:
        return redirect(reverse('home.home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.password == password:
            request.session['user_id'] = user.id
            messages.success(request, 'Logged in successfully!')
            next_page = request.GET.get('next')
            return redirect(next_page) if next_page else redirect(reverse('home.home'))

        messages.error(request, 'Invalid username or password.')

    return render_template(request, 'login.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    request.session.pop('user_id', None)
    messages.info(request, 'You have been logged out.')
    return redirect(reverse('auth.login'))


@csrf_exempt
def register_view(request: HttpRequest) -> HttpResponse:
    current_user = get_current_user(request)
    if current_user.is_authenticated:
        return redirect(reverse('home.home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
        else:
            new_user = User.objects.create(username=username, password=password, role=role)
            request.session['user_id'] = new_user.id
            messages.success(request, 'Account created successfully!')
            return redirect(reverse('home.home'))

    return render_template(request, 'register.html')


def _videos_folder() -> str:
    return os.path.join(settings.BASE_DIR, 'app', 'static', 'videos')


@login_required
def live_feed(request: HttpRequest) -> HttpResponse:
    videos_folder = _videos_folder()
    if not os.path.exists(videos_folder):
        return JsonResponse({'error': 'Videos folder not found.'}, status=404)

    video_files = [
        f for f in os.listdir(videos_folder)
        if f.lower().endswith(('.mp4', '.webm', '.ogg'))
    ]

    if not video_files:
        return JsonResponse({'error': 'No video files found.'}, status=404)

    video_urls = [f"{settings.STATIC_URL}videos/{video}" for video in video_files]

    return render_template(request, 'feed.html', {'video_urls': video_urls})


def preprocess_frame(frame):
    frame = cv2.resize(frame, (299, 299))
    frame = frame / 255.0
    frames = np.repeat(np.expand_dims(frame, axis=0), 10, axis=0)
    frames = np.expand_dims(frames, axis=0)
    return frames


@csrf_exempt
def predict(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    model = _get_ml_model()
    if model is None:
        return JsonResponse({'error': 'Model not available. Please check if the model file exists.'}, status=503)

    if 'video_frame' not in request.FILES:
        return JsonResponse({'error': 'No video frame provided'}, status=400)

    file = request.FILES['video_frame']
    np_img = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    processed_frame = preprocess_frame(frame)
    predictions = model.predict(processed_frame)
    anomaly_score = float(predictions[0][0])

    return JsonResponse({'anomaly_score': anomaly_score})


def _format_dt(dt: datetime | None) -> str:
    if not dt:
        return ''
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def _parse_dt_str(value: str | None) -> datetime | None:
    if not value:
        return None

    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S'):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    return None


@login_required
def history_home(request: HttpRequest) -> HttpResponse:
    anomalies_query = Anomaly.objects.order_by('-timestamp').all()
    alarm_history_query = AlarmHistory.objects.order_by('-start_time').all()

    anomalies = [
        {
            'id': a.id,
            'location': a.location or '',
            'camera_id': a.camera_id or '',
            'ipaddress': a.ipaddress or '',
            'anomaly_code': a.anomaly_code or '',
            'anomaly_name': a.anomaly_name or '',
            'timestamp': _format_dt(a.timestamp),
            'duration': a.duration or '',
            'confidence': a.confidence or '',
            'status': a.status or '',
            'actions_taken': a.actions_taken or '',
            'videopath': a.videopath or '',
        }
        for a in anomalies_query
    ]

    alarm_history = [
        {
            'id': r.id,
            'room': r.room,
            'location': r.location or '',
            'activated_by': r.activated_by,
            'start_time': _format_dt(r.start_time),
            'end_time': _format_dt(r.end_time) if r.end_time else '',
            'duration': r.duration or '',
        }
        for r in alarm_history_query
    ]

    return render_template(request, 'history.html', {'anomalies': anomalies, 'alarm_history': alarm_history})


@csrf_exempt
@login_required
def history_add(request: HttpRequest) -> HttpResponse:
    record_type = request.GET.get('record_type', 'anomaly')

    if request.method == 'POST':
        if request.content_type and 'application/json' in request.content_type:
            try:
                data = json.loads(request.body.decode('utf-8'))
            except Exception:
                data = {}
        else:
            data = request.POST

        if record_type == 'alarm':
            room = data.get('room')
            location = data.get('location')
            activated_by = data.get('activated_by')
            start_time = _parse_dt_str(data.get('start_time'))
            end_time = _parse_dt_str(data.get('end_time'))
            duration = data.get('duration')

            new_record = AlarmHistory(
                room=room,
                location=location,
                activated_by=activated_by,
                start_time=start_time or datetime.utcnow(),
                end_time=end_time,
                duration=float(duration) if duration not in (None, '') else None,
            )
            new_record.save()
            messages.success(request, 'Alarm history added successfully!')
        else:
            duration = data.get('duration')
            confidence = data.get('confidence')

            new_record = Anomaly(
                location=data.get('location'),
                camera_id=data.get('camera_id'),
                ipaddress=data.get('ipaddress'),
                anomaly_code=data.get('anomaly_code'),
                anomaly_name=data.get('anomaly_name'),
                duration=float(duration) if duration not in (None, '') else None,
                confidence=float(confidence) if confidence not in (None, '') else None,
                status=data.get('status'),
                actions_taken=data.get('actions_taken'),
                videopath=data.get('videopath'),
            )
            new_record.save()
            messages.success(request, 'Anomaly added successfully!')

        return redirect(f"{reverse('history.home')}?record_type={record_type}")

    return render_template(request, 'add_record.html', {'record_type': record_type})


@csrf_exempt
@login_required
def history_edit(request: HttpRequest, record_id: int) -> HttpResponse:
    current_user = get_current_user(request)
    if current_user.role != 'admin':
        return render_template(request, 'errors/403.html', status=403)

    record_type = request.GET.get('record_type', 'anomaly')

    if record_type == 'alarm':
        record = AlarmHistory.objects.filter(id=record_id).first()
    else:
        record = Anomaly.objects.filter(id=record_id).first()

    if not record:
        return render_template(request, 'errors/404.html', status=404)

    if request.method == 'POST':
        if record_type == 'alarm':
            record.start_time = _parse_dt_str(request.POST.get('start_time')) or record.start_time
            record.end_time = _parse_dt_str(request.POST.get('end_time'))
            duration = request.POST.get('duration')
            record.duration = float(duration) if duration not in (None, '') else None
            record.save()
            messages.success(request, 'Alarm history updated successfully!')
        else:
            record.anomaly_code = request.POST.get('anomaly_code')
            record.anomaly_name = request.POST.get('anomaly_name')
            record.status = request.POST.get('status')
            record.actions_taken = request.POST.get('actions_taken')
            record.save()
            messages.success(request, 'Anomaly updated successfully!')

        return redirect(f"{reverse('history.home')}?record_type={record_type}")

    return render_template(request, 'edit_record.html', {'record': record, 'record_type': record_type})


alarms = [
    {'id': 1, 'room': 'Lobby', 'location': 'Main Lobby', 'active': False},
    {'id': 2, 'room': 'Entrance', 'location': 'Main Entrance', 'active': False},
    {'id': 3, 'room': 'Reading Hall', 'location': 'Reading Hall', 'active': False},
    {'id': 4, 'room': 'Balcony', 'location': 'Second Floor Balcony', 'active': False},
    {'id': 5, 'room': 'Conference Room', 'location': 'Third Floor Conference Room', 'active': False},
    {'id': 6, 'room': 'Cafeteria', 'location': 'Ground Floor Cafeteria', 'active': False},
    {'id': 7, 'room': 'Restroom', 'location': 'First Floor Restroom', 'active': False},
    {'id': 8, 'room': 'Parking Lot', 'location': 'Underground Parking', 'active': False},
    {'id': 9, 'room': 'Elevator', 'location': 'Central Elevator', 'active': False},
    {'id': 10, 'room': 'Staircase', 'location': 'North Staircase', 'active': False},
]


@admin_required
def broadcast_home(request: HttpRequest) -> HttpResponse:
    return render_template(request, 'broadcast.html', {'alarms': alarms})


@admin_required
def broadcast_toggle(request: HttpRequest, id: int) -> HttpResponse:
    current_user = get_current_user(request)

    for alarm in alarms:
        if alarm['id'] == id:
            new_state = not alarm['active']
            alarm['active'] = new_state
            if new_state:
                AlarmHistory.objects.create(
                    room=alarm['room'],
                    location=alarm['location'],
                    activated_by=current_user.username or '',
                )
            else:
                record = AlarmHistory.objects.filter(id=alarm['id'], end_time__isnull=True).order_by('-start_time').first()
                if record:
                    record.end_time = datetime.utcnow()
                    record.duration = (record.end_time - record.start_time).total_seconds()
                    record.save()

            messages.info(request, f"Alarm in {alarm['room']} toggled to {'active' if new_state else 'inactive'}.")
            break
    else:
        messages.error(request, 'Alarm not found.')

    return redirect(reverse('broadcast.home'))


@csrf_exempt
@admin_required
def broadcast_voice(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=405)

    messages.info(request, 'Voice message received and broadcasted.')
    return HttpResponse('OK', status=200)


def analytics_home(request: HttpRequest) -> HttpResponse:
    return render_template(request, 'analytics.html')


def get_analytics_data(request: HttpRequest) -> JsonResponse:
    anomalies_query = Anomaly.objects.all()
    alarm_history_query = AlarmHistory.objects.all()

    anomalies = [
        {
            'id': a.id,
            'location': a.location or '',
            'camera_id': a.camera_id or '',
            'ipaddress': a.ipaddress or '',
            'anomaly_code': a.anomaly_code or '',
            'anomaly_name': a.anomaly_name or '',
            'timestamp': _format_dt(a.timestamp),
            'duration': a.duration if a.duration is not None else 0,
            'confidence': a.confidence if a.confidence is not None else 0,
            'status': a.status or 'Unknown',
            'actions_taken': a.actions_taken or '',
            'videopath': a.videopath or '',
        }
        for a in anomalies_query
    ]

    alarm_history = [
        {
            'id': r.id,
            'room': r.room,
            'location': r.location or '',
            'activated_by': r.activated_by,
            'start_time': _format_dt(r.start_time),
            'end_time': _format_dt(r.end_time) if r.end_time else '',
            'duration': r.duration if r.duration is not None else 0,
        }
        for r in alarm_history_query
    ]

    return JsonResponse({'anomalies': anomalies, 'alarm_history': alarm_history})
