#!/usr/bin/env python
import pika, sys, os

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='busqueda_medios')

    def iniciar_busqueda(ch, method, properties, body):
        print("starting search for:")
        print(ch)
        print(method)
        print(properties)
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='busqueda_medios', on_message_callback=iniciar_busqueda, auto_ack=True)

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
