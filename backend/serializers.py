from rest_framework import serializers
from .models import Receipt, Item


# item serializer for items on receipt
class ItemSerializer(serializers.ModelSerializer):
    receipt = serializers.ReadOnlyField(source="receipt.id")

    class Meta:
        model = Item
        fields = ["shortDescription", "price", "receipt"]

    def create(self, validated_data):
        validated_data["shortDescription"] = validated_data["shortDescription"].strip()
        return Item.objects.create(**validated_data)


# receipt serializer
class ReceiptSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        items = validated_data.pop("items")

        if len(items) < 1:
            raise serializers.ValidationError(
                {"items": "Please enter the amount of items on receipt"}
            )
        receipt = Receipt.objects.create(**validated_data)

        for item in items:
            new_item = Item(receipt=receipt)
            serializer = ItemSerializer(new_item, data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                raise serializers.ValidationError(serializer.errors)

        return receipt

    items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = "__all__"
