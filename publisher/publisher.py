#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='busqueda_medios')

channel.basic_publish(exchange='', routing_key='busqueda_medios', body='{"ambito":"CAM","medios":"todos","claves":"todas","username":"odeen","client","Cntest"}')
print(" [x] Sent search request'")
connection.close()
