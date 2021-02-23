#!/usr/bin/env python
import pika, sys, os, time

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='busqueda_medios_durable', durable=True)

    def iniciar_busqueda(ch, method, properties, body):
        print(" [x] Received %r" % body)
        print("stopping for 3 seconds")
        time.sleep(3)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='busqueda_medios', on_message_callback=iniciar_busqueda)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
