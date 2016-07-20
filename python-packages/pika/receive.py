import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

users = []

def do_thing_with_user(user_id):
    users.append(user_id)
    print users

def callback(ch, method, properties, body):
    data = json.loads(body)
    do_thing_with_user(data['user_id'])

channel.basic_consume(callback, queue='hello',no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
