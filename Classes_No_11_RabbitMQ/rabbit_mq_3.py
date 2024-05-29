import pika
from sys import argv
from time import sleep


def send(channel):
    #msg = argv[2]
    for i in range(20):
        channel.basic_publish(exchange='', routing_key='letterbox', body=str(i))
        print(f'Message {i} published')


def receive(channel):
    delay = float(argv[2])
    def consume(channel, method, props, body: bytes):
        print(f'Received message {body.decode()}')
        sleep(delay)
        channel.basic_ack(delivery_tag = method.delivery_tag)
        print('Processed message')
    channel.basic_consume(queue = 'letterbox', on_message_callback = consume)
    print('Start consuming')
    channel.start_consuming()

conn_pars = pika.ConnectionParameters('localhost')
with pika.BlockingConnection(conn_pars) as conn:
        channel = conn.channel()
        channel.queue_declare(queue = 'letterbox')
        if argv[1] == 'send':
             send(channel)
        else:
             receive(channel)