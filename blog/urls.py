from django.urls import path

from .views import home, about, myposts

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
    path('myposts/', myposts , name='myposts'),
    
]
