#!/usr/bin/env python

import confluent_kafka


with open('messages', 'rt') as f:
    lines = f.readlines()

messages = [line.strip() for line in lines]

# Kafka broker address and port
config = {
    'bootstrap.servers': 'localhost:9092',
    'api.version.request': False
}

p = confluent_kafka.Producer(config)
for m in messages:
    p.produce('test_topic', m)

p.flush()
