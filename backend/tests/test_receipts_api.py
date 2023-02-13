from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status, serializers


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

    # def test_create_invalid_receipt_no_items(self):
    #     response = self.client.post(
    #         reverse("receipts"),
    #         data=self.invalid_receipt_no_items,
    #         format="json",
    #     )
    #     # print(response.errors)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertRaises(serializers.ValidationError)

    # def test_create_invalid_receipt_no_retailer(self):
    #     response = self.client.post(
    #         reverse("receipts"),
    #         data=self.invalid_receipt_no_retailer,
    #         format="json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_receipt(self):
        for i in self.valid_receipt.keys():
            test_receipt = dict(self.valid_receipt)
            test_receipt[i] = ""
            # print(test_receipt)
            response = self.client.post(
                reverse("receipts"), data=test_receipt, format="json"
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
