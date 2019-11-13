# producer
import pika

#instance of Connection object
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#new channel (can pass channel number)
channel = connection.channel()

#declare/create queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World! yo')

print("[x] Sent 'Hello World! eyyy'")

connection.close()
