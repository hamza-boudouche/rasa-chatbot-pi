import json


def send(channel, exchange_name, routing_key, message):
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
    message_text = json.dumps(message)
    channel.basic_publish(exchange=exchange_name,
                          routing_key=routing_key,
                          body=message_text)
