from rest_framework import serializers
from .models import Receipt, Item


# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = "__all__"


class ItemSerializer(serializers.Serializer):
    shortDescription = serializers.CharField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)


class ReceiptSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        items = validated_data.pop("items")

        receipt = Receipt.objects.create(**validated_data)

        for item in items:
            item = Item.objects.create(receipt=receipt, **item)

        return receipt

    items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = "__all__"
