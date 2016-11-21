# Apache Kafka demonstration environment

A simple virtual machine environment with an Apache Kafka installation and
some sample scripts.


## Requirements

- Vagrant
- VirtualBox


## Instructions

1. Run `vagrant up` to create and provision the virtual machine.
2. Log into it with `vagrant ssh`.
3. Start Apache ZooKeeper by running `sudo systemctl start zookeeper`.
4. Start Apache Kafka by running `sudo systemctl start kafka`.

The *code* folder contains some scripts demonstrating how to use Apache Kafka
with the *confluent-python* package.
