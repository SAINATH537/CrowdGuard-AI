# SafeSight Integration Bridge
# Connects landing page to main application seamlessly

from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponse

def landing_redirect(request):
    """Redirect from landing page to main app with seamless integration"""
    if request.path == '/' or request.path == '/home':
        # Check if user is authenticated and redirect appropriately
        if request.user.is_authenticated if hasattr(request, 'user') else False:
            return redirect('/dashboard/')
        else:
            # Show integrated landing page with login options
            return redirect('/auth/login')
    return redirect('/dashboard/')

def integrated_home(request):
    """Integrated home that works for both marketing and app"""
    return render_template(request, 'dashboard.html')

# URL patterns for seamless integration
urlpatterns = [
    path('', landing_redirect, name='landing.redirect'),
    path('home/', landing_redirect, name='landing.home.redirect'),
    path('dashboard/', integrated_home, name='integrated.dashboard'),
]
