from django.urls import path
from . import views

urlpatterns = [
    path("", views.home)
]
#update each time a new function is made in views.py