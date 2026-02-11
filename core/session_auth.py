from dataclasses import dataclass
from functools import wraps

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from .models import User


@dataclass
class SessionUser:
    id: int | None
    username: str | None
    role: str | None
    is_authenticated: bool


def get_current_user(request: HttpRequest) -> SessionUser:
    user_id = request.session.get('user_id')
    if not user_id:
        return SessionUser(id=None, username=None, role=None, is_authenticated=False)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        request.session.pop('user_id', None)
        return SessionUser(id=None, username=None, role=None, is_authenticated=False)

    return SessionUser(id=user.id, username=user.username, role=user.role, is_authenticated=True)


def login_required(view_func):
    @wraps(view_func)
    def _wrapped(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = get_current_user(request)
        if not user.is_authenticated:
            login_url = reverse('auth.login')
            return redirect(f"{login_url}?next={request.get_full_path()}")
        return view_func(request, *args, **kwargs)

    return _wrapped


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = get_current_user(request)
        if not user.is_authenticated:
            return redirect(reverse('auth.login'))
        if user.role != 'admin':
            from .rendering import render_template
            return render_template(request, 'errors/403.html', status=403)
        return view_func(request, *args, **kwargs)

    return _wrapped
