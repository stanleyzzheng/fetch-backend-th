from django.db import models
import uuid


# Create your models here.


class Item(models.Model):
    shortDescription = models.CharField(max_length=250, blank=False, null=False)

    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    receipt = models.ForeignKey(
        "Receipt",
        related_name="items",
        on_delete=models.CASCADE,
    )


class Receipt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # items = models.JSONField()
    retailer = models.CharField(max_length=250, blank=False, null=False)
    purchaseDate = models.DateField(blank=False, null=False)
    purchaseTime = models.TimeField(blank=False, null=False)
    # Allow max totals of 999999.99
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    points = models.IntegerField()

    def get_points(self):
        points = 0

        return self.total
