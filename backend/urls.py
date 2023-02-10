from django.urls import path
from . import views

urlpatterns = [
    path("process/", views.process),
    path("<str:pk>/points/", views.points),
]
