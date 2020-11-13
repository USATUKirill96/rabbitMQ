from __future__ import absolute_import

import json

import pika

from celery import shared_task

from apps.tablet.services import create_order


@shared_task
def tablet2_consumer():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='fanout', exchange_type='fanout')

    result = channel.queue_declare(queue='tablet', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='fanout', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        create_order(data)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
