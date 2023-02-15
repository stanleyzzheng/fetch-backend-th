from django.shortcuts import render
from .models import Receipt
from .serializers import ReceiptSerializer
from rest_framework import status

# Create your views here.
from rest_framework.decorators import (
    api_view,
)
from rest_framework.response import Response
from .utils import get_points


# POST request for posting receipt data
@api_view(["POST"])
def process(request):
    if request.method == "POST":
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"id": serializer.data["id"]}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  GET all receipts from database
@api_view(["GET"])
def get_all_receipts(request):
    if request.method == "GET":
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# get single receipt
@api_view(["GET", "DELETE"])
def get_receipt_detail(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
    except Receipt.DoesNotExist:
        return Response(
            {"error": "receipt with id you request could not be found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        receipt.delete()
        return Response({f"{pk} deleted"}, status=status.HTTP_204_NO_CONTENT)


# GET points with args: pk
@api_view(["GET"])
def points(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
    except Receipt.DoesNotExist:
        return Response(
            {"error": "receipt with id you request could not be found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = ReceiptSerializer(receipt)

        points = get_points(
            retailer=serializer.data["retailer"],
            items=serializer.data["items"],
            purchaseDate=serializer.data["purchaseDate"],
            purchaseTime=serializer.data["purchaseTime"],
            total=serializer.data["total"],
        )
        # p = get_points(retailer, items, purchaseDate, purchaseTime, total)
        # print(p)

        return Response({"points": points}, status=status.HTTP_200_OK)
