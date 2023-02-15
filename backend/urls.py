from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_receipts, name="get_all_receipts"),
    path("process/", views.process, name="receipts"),
    path("<str:pk>/", views.get_receipt_detail, name="receipt_detail"),
    path("<str:pk>/points/", views.points, name="points"),
]
