# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class TabletOrder(models.Model):
    name = models.CharField(max_length=250)
    order_id = models.IntegerField()
    quantity = models.IntegerField()
    delivery_at = models.DateTimeField()

    def __str__(self):
        return self.name
