import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

content = {'user_id': 30031}

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(content)
)

print("[x] Sent {0}".format(content))
connection.close()
