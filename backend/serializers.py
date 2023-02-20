from rest_framework import serializers
from .models import Receipt, Item


# item serializer
class ItemSerializer(serializers.ModelSerializer):
    # include receipt id for storage
    receipt = serializers.ReadOnlyField(source="receipt.id")
    # class meta for base
    class Meta:
        model = Item
        fields = ["shortDescription", "price", "receipt"]
    # redefine create because some extra data validation is needed
    def create(self, validated_data):
        # strip shortDescription from whitespace for cleaner data
        validated_data["shortDescription"] = validated_data["shortDescription"].strip()
        return Item.objects.create(**validated_data)


# receipt serializer
class ReceiptSerializer(serializers.ModelSerializer):
    """Serializer for receipts which maintains integrity of the receipt input from users."""

    # Redefine create which allows for nested serialization of items
    def create(self, validated_data):
        items = validated_data.pop("items")
        # validator to ensure items array is > 1
        if len(items) < 1:
            # raise validation error otherwise
            raise serializers.ValidationError(
                {"items": "Please enter the amount of items on receipt"}
            )
        # create receipt objects based off of validated data
        receipt = Receipt.objects.create(**validated_data)
        # serialize item data
        for item in items:
            new_item = Item(receipt=receipt)
            serializer = ItemSerializer(new_item, data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                raise serializers.ValidationError(serializer.errors)
        # return receipt object for storage when data is validated
        return receipt
    # serialize items in order for readability
    items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = "__all__"
