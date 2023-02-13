from django.urls import path
from . import views

urlpatterns = [
    path("process/", views.process, name="receipts"),
    path("<str:pk>/points/", views.points, name="points"),
]
