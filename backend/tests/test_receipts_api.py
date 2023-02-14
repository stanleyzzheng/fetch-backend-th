from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Receipt, Item
from ..serializers import ReceiptSerializer


class TestGetReceiptDetailAndPoints(APITestCase):
    """Test module for GET single Receipt API and points for the receipt"""

    test_receipt = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ],
        "total": "9.00",
    }

    def setUp(self):
        serializer = ReceiptSerializer(data=self.test_receipt)
        if serializer.is_valid():
            serializer.save()
            self.valid_receipt = serializer.data

    def test_get_valid_single_receipt(self):
        response = self.client.get(
            reverse("receipt_detail", kwargs={"pk": self.valid_receipt["id"]}),
        )
        receipt = Receipt.objects.get(pk=self.valid_receipt["id"])
        serializer = ReceiptSerializer(receipt)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_correct_points(self):
        response = self.client.get(
            reverse("points", kwargs={"pk": self.valid_receipt["id"]})
        )
        self.assertEqual(response.data["points"], 109)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestReceiptCreate(APITestCase):
    """Test Module for POST Receipts API"""

    def setUp(self):
        self.valid_receipt = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
            ],
            "total": "9.00",
        }

    def test_create_valid_receipt(self):
        response = self.client.post(
            reverse("receipts"), data=self.valid_receipt, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_receipt(self):
        for i in self.valid_receipt.keys():
            test_receipt = dict(self.valid_receipt)
            test_receipt[i] = ""
            # print(test_receipt)
            response = self.client.post(
                reverse("receipts"), data=test_receipt, format="json"
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
