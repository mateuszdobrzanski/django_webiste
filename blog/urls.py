from django.urls import path
from . import views

urlpatterns = [
    # first empty string is mean homepage
    # second file . method
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
