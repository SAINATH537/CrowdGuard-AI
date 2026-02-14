from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render
from core import views
import os


# Serve the local Django landing template by default. Previously this endpoint
# redirected to an external Next.js server on http://localhost:3000 which causes
# "connection refused" when the frontend dev server isn't running. To make the
# Django app self-contained during development we render `home.html` locally.
def redirect_to_frontend(request):
    # Allow opt-in to external landing via environment variable
    use_external = os.environ.get('USE_EXTERNAL_LANDING', '') == '1'
    if use_external:
        return HttpResponse(
            '<meta http-equiv="refresh" content="0;url=http://localhost:3000">',
            status=302,
        )
    # Render the Django template `home.html` from the app templates
    try:
        return render(request, 'home.html')
    except Exception:
        # Fallback: simple informative HTML if template rendering fails
        return HttpResponse(
            '<h1>SafeSight</h1><p>Landing page not available. Check templates/home.html</p>'
        )

urlpatterns = [
    path('', redirect_to_frontend, name='redirect.frontend'),
    path('api/', include('core.urls')),
    path('auth/login/', views.login_view, name='auth.login.slash'),
    path('auth/login', views.login_view, name='auth.login'),
    path('auth/logout/', views.logout_view, name='auth.logout.slash'),
    path('auth/logout', views.logout_view, name='auth.logout'),
    path('auth/register/', views.register_view, name='auth.register.slash'),
    path('auth/register', views.register_view, name='auth.register'),
    path('feed/', views.live_feed, name='feed.live_feed'),
    path('feed', views.live_feed, name='feed.live_feed.noslash'),
    path('api/predict', views.predict, name='api.predict'),
    path('history/', views.history_home, name='history.home'),
    path('history', views.history_home, name='history.home.noslash'),
    path('history/add', views.history_add, name='history.add'),
    path('history/add/', views.history_add, name='history.add.slash'),
    path('history/edit/<int:record_id>', views.history_edit, name='history.edit'),
    path('broadcast/', views.broadcast_home, name='broadcast.home'),
    path('broadcast', views.broadcast_home, name='broadcast.home.noslash'),
    path('broadcast/toggle/<int:id>', views.broadcast_toggle, name='broadcast.toggle'),
    path('broadcast/toggle/<int:id>/', views.broadcast_toggle, name='broadcast.toggle.slash'),
    path('broadcast/voice', views.broadcast_voice, name='broadcast.voice'),
    path('broadcast/voice/', views.broadcast_voice, name='broadcast.voice.slash'),
    path('analytics/', views.analytics_home, name='analytics.home'),
    path('analytics', views.analytics_home, name='analytics.home.noslash'),
    path('analytics/get-analytics-data', views.get_analytics_data, name='analytics.get_analytics_data'),
    path('analytics/get-analytics-data/', views.get_analytics_data, name='analytics.get_analytics_data.slash'),
    path('admin/', admin.site.urls),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) if hasattr(settings, 'STATIC_ROOT') else []
