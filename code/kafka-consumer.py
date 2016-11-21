#!/usr/bin/env python

import confluent_kafka


config = {
    'bootstrap.servers': 'localhost:9092', # Kafka broker address and port
    'group.id': 'mygroup',
    'api.version.request': False,
    'default.topic.config': {
        'auto.offset.reset': 'smallest',
    },
}

c = confluent_kafka.Consumer(config)
c.subscribe(['test_topic'])

running = True
while running:
    try:
        msg = c.poll(1.0)
        if msg is None:
            continue
        elif not msg.error():
            print(msg.value())
        elif msg.error().code() != confluent_kafka.KafkaError._PARTITION_EOF:
            print(msg.error())
            running = False
    except KeyboardInterrupt:
        running = False

c.close()
