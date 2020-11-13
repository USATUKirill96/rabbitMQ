# coding=utf-8
from __future__ import unicode_literals

# thirdparty
from datetime import datetime

from kombu.transport.virtual.exchange import ExchangeType, FanoutExchange
from rest_framework.response import Response
from rest_framework.views import APIView
from .schemas import OrderSchema, TabletOrderSchema
import pika

# project
from .models import ErpOrder


class RequestSchema(OrderSchema):
    pass


class OrderView(APIView):

    def post(self, request):

        date = datetime.now()
        order = ErpOrder.objects.create(name=request.data["name"],
                                        quantity=request.data["quantity"],
                                        delivery_at=date,
                                        address=request.data["address"]
                                        )
        order.save()
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='orders')

        channel.basic_publish(exchange="", routing_key='orders', body=TabletOrderSchema().dumps(order))
        connection.close()
        return Response(status=200)
