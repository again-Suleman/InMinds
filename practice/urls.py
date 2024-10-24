"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Login
from django.contrib.auth.views import LoginView, LogoutView

# Register 
from user.views import register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    
    # Login Stuff
    path('login/', LoginView.as_view(template_name='user/login.html', next_page='blog-home'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html', next_page='login'), name='logout'),
]



# Instructing Django from where to serve
if settings.DEBUG:  # Only in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
