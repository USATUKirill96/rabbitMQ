# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class ErpOrder(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    delivery_at = models.DateTimeField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name
