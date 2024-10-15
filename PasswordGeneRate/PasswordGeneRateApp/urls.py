from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generator/", views.generator, name="generator"),
    path("insultor/", views.insultor, name="insultor"),
    path("privacy_policy/", views.privacy, name="privacy"),
]
#update each time a new function is made in views.py