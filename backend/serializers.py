from rest_framework import serializers
from .models import Receipt, Item


# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = "__all__"


# class ItemSerializer(serializers.Serializer):
#     shortDescription = serializers.CharField()
#     price = serializers.DecimalField(max_digits=7, decimal_places=2)

#     def create(self, validated_data):
#         validated_data["shortDescription"] = validated_data["shortDescription"].strip()
#         print(validated_data)
#         return Item.objects.create(**validated_data)


class ItemSerializer(serializers.ModelSerializer):
    # shortDescription = serializers.CharField()
    # price = serializers.DecimalField(max_digits=7, decimal_places=2)
    # receipt = serializers.SlugRelatedField(
    #     queryset=Receipt.objects.all(), slug_field="id"
    # )
    receipt = serializers.ReadOnlyField(source="receipt.id")

    class Meta:
        model = Item
        fields = ["shortDescription", "price", "receipt"]

    def create(self, validated_data):
        validated_data["shortDescription"] = validated_data["shortDescription"].strip()
        return Item.objects.create(**validated_data)


class ReceiptSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        items = validated_data.pop("items")

        if len(items) < 1:
            raise serializers.ValidationError(
                {"items": "Please enter the amount of items on receipt"}
            )
        receipt = Receipt.objects.create(**validated_data)

        for item in items:
            # newItem = {**item}
            # newItem["receipt"] = receipt.id
            # print(newItem)
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
