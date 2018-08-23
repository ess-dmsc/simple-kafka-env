# Apache Kafka demonstration environment

A simple virtual machine environment with an Apache Kafka installation.


## Requirements

- Vagrant
- VirtualBox


## Instructions

1. Run `vagrant up` to create and provision the virtual machine.
2. Log into it with `vagrant ssh`.
3. Start Apache ZooKeeper by running `sudo systemctl start dm-zookeeper`.
4. Start Apache Kafka by running `sudo systemctl start dm-kafka`.


## Manually checking Kafka is working

Open two separate terminal windows, log into the VM and go to
*/opt/dm_group/kafka/bin*. In one of them, start a Kafka consumer subscribing
to the `test_topic` topic by running

    $ ./kafka-console-consumer.sh --zookeeper 192.168.100.11:2181 --topic test_topic

In the other terminal window, start a producer with

    $ ./kafka-console-producer.sh --broker-list 192.168.100.11:9092 --topic test_topic

On the producer screen, type a message and press `Return`. You should receive
it on the consumer screen.
