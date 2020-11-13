# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class DriveOrder(models.Model):
    order_id = models.IntegerField()
    delivery_at = models.DateTimeField()
