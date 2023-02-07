from django.shortcuts import render
from .models import Receipt

# Create your views here.
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response


@api_view(["POST"])
def process(request):
    if request.method == "POST":
        print(request.data)
        return Response(request.data)
