import pika
from sys import argv

def send(channel):
    msg = argv[2]
    props = pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
    channel.basic_publish(exchange='', routing_key='letterbox', body=msg, properties=props)
    print(f'Message {msg} published')

def receive(channel):
    def consume(channel, method, props, body):
        print(f'Received message {body}')
    channel.basic_consume(queue = 'letterbox', auto_ack = True,
                          on_message_callback = consume)
    print('Start consuming')
    channel.start_consuming()

conn_pars = pika.ConnectionParameters('localhost')
with pika.BlockingConnection(conn_pars) as conn:
        channel = conn.channel()
        channel.queue_declare(queue = 'letterbox', durable = True)
        if argv[1] == 'send':
             send(channel)
        else:
             receive(channel)