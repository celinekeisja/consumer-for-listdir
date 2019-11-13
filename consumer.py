# consumer
import pika
import configparser
import os
import sys
import logging
import time


def connect(hostname):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
    return connection


def channel(connection, queue_name):
    ch = connection.channel()
    ch.queue_declare(queue=queue_name)
    return ch


def callback(ch, method, properties, body):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    connect(config['queue']['hostname']).sleep(int(config['queue']['time_to_sleep']))
    logging.info("[x] Received {}".format(body))


def consume(chnnl, queue_name):
    chnnl.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages. To exit, press CTRL+C')
    chnnl.start_consuming()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    o = os.path.dirname(__file__)
    config.read(o+'config.ini')
    hname = config['queue']['hostname']
    qname = config['queue']['queue_name']
    consume(channel(connect(hname), qname), qname)
