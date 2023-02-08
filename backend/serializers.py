from rest_framework import serializers
from .models import Receipt


# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = "__all__"


class ReceiptSerializer(serializers.ModelSerializer):
    # items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = "__all__"
