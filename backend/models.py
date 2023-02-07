from django.db import models


# Create your models here.
class Receipt(models.Model):
    id = models.UUIDField(primary_key=True)
    total = models.IntegerField()
