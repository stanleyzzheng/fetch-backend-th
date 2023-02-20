from django.db import models
import uuid
from .utils import get_points

# Create your models here.


class Item(models.Model):
    """Item Model which allows item data to be successfully input with receipts"""

    shortDescription = models.CharField(max_length=250, blank=False, null=False)

    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    receipt = models.ForeignKey(
        "Receipt",
        related_name="items",
        on_delete=models.CASCADE,
    )


class Receipt(models.Model):
    """Receipt model which allows receipt data to be stored onto database

    Args:
        id: Primary key, uuid
        retailer (string): name of retailer
        purchaseDate(date): date the receipt was processed
        purchaseTime(time): time the receipt was processed
        total(float): float amount of total
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # items = models.JSONField()
    retailer = models.CharField(max_length=250, blank=False, null=False)
    purchaseDate = models.DateField(blank=False, null=False)
    purchaseTime = models.TimeField(blank=False, null=False)
    # Allow max totals of 999999.99
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
