import json
import pika

from celery import shared_task

from apps.drive.services import create_order


@shared_task
def drive_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='orders')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        create_order(data)

    channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

