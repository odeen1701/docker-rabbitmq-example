#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='busqueda_medios_durable', durable=True)
for i in range(30):
    channel.basic_publish(exchange='', routing_key='busqueda_medios', body='-->xx {} xx<--'.format(i), properties=pika.BasicProperties(delivery_mode=2)) #delivery_mode=2 -> message is persistent
    print(" [x] Sent search request'")

connection.close()
