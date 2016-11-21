#!/usr/env/bin python

import confluent_kafka


with open('messages', 'rt') as f:
    lines = f.readlines()

messages = [line.strip() for line in lines]

# Kafka broker address and port
config = {'bootstrap.servers': 'localhost:9092'}

p = confluent_kafka.Producer(config)
print(messages)
for m in messages:
    print(m)
    p.produce('test_topic', m)

p.flush()
