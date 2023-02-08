from django.shortcuts import render
from .models import Receipt
from .serializers import ReceiptSerializer
from rest_framework import status

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
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
