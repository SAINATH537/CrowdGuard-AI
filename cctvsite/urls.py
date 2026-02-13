from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from core import views

# Keep original home page redirect to landing page
def redirect_to_frontend(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>SafeSight - AI Security Platform</title>
            <meta http-equiv="refresh" content="0;url=http://localhost:3000">
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    background: linear-gradient(135deg, #0057D9 0%, #004299 100%);
                    color: white; 
                    text-align: center; 
                    padding: 50px; 
                    margin: 0;
                    min-height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                .container { 
                    max-width: 600px; 
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    border-radius: 16px;
                    padding: 40px;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                }
                .logo { 
                    font-size: 3rem; 
                    font-weight: bold; 
                    margin-bottom: 20px;
                    display: flex;
                    align-items: center;
                    gap: 15px;
                }
                .title { 
                    font-size: 2rem; 
                    margin-bottom: 15px;
                    font-weight: 600;
                }
                .subtitle { 
                    font-size: 1.1rem; 
                    margin-bottom: 30px;
                    opacity: 0.9;
                }
                .links { 
                    display: flex; 
                    gap: 20px; 
                    justify-content: center;
                    flex-wrap: wrap;
                }
                .link { 
                    background: rgba(255, 255, 255, 0.2);
                    color: white; 
                    text-decoration: none; 
                    padding: 12px 24px;
                    border-radius: 8px;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    transition: all 0.3s ease;
                    font-weight: 500;
                }
                .link:hover {
                    background: rgba(255, 255, 255, 0.3);
                    transform: translateY(-2px);
                }
                .shield {
                    width: 60px;
                    height: 60px;
                    background: rgba(255, 255, 255, 0.2);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 2rem;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <div class="shield">🛡️</div>
                    <span>SafeSight</span>
                </div>
                <h1 class="title">AI-Powered Security Platform</h1>
                <p class="subtitle">Real-time threat detection and response system</p>
                <div class="links">
                    <a href="http://localhost:3000" class="link">🏠 Landing Page</a>
                    <a href="/feed/" class="link">📹 Live Feed</a>
                    <a href="/auth/login" class="link">🔐 Login</a>
                    <a href="/admin/" class="link">⚙️ Admin</a>
                </div>
            </div>
        </body>
    </html>
    """)

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
