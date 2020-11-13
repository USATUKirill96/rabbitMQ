# coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class DriveConfig(AppConfig):
    name = "apps.drive"

    def ready(self):
        from .tasks import drive_consumer
        drive_consumer.apply_async(countdown=1)

