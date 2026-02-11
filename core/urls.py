from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home.home'),
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
]
