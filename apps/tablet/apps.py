# coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class TabletConfig(AppConfig):
    name = "apps.tablet"

    def ready(self):
        from .tasks import tablet2_consumer
        tablet2_consumer.apply_async(countdown=1)
