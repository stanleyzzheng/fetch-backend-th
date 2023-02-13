from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Receipt


class TestGetPoints(APITestCase):
    test_receipt = Receipt(
        {
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
    )

    def setUp(self):
        self.receipt = Receipt.objects.create(**self.test_receipt)


class TestReceiptCreate(APITestCase):
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
