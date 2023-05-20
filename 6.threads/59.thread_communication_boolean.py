# Thread communication
"""
There is a common pattern followed, namely producer thread and consumer thread.
the producer thread is responsible for creating some work
    example: the producer thread will be responsible for creating an order with all the items
            the consumer thread will be responsible for consuming the order and processing them

            Here is the producer thread will have a booloean of placeOrder = False
            the consumer thread will continuosly monitor the boolean. The the boolean is
            true, the consumer will take the order and process it.


"""

# Using the boolean for communication
from threading import *
from time import *


class Producer:
    def __init__(self) -> None:
        self.products = []
        self.ordersPlace = False
        
    def produce(self):
        print(current_thread().name)
        for i in range(1, 6):
            self.products.append("Product " + str(i))
            sleep(1)
            print("Item Added.")

        self.ordersPlace = True


class Consumer:
    def __init__(self, producer) -> None:
        self.producer = producer
        
    def consume(self):
        print(current_thread().name)
        while self.producer.ordersPlace == False:
            print("Waiting for the orders")
            sleep(0.2) # Not neccessary using for example
        print("Orders place ", self.producer.products)


p = Producer()
pt = Thread(target=p.produce)

c = Consumer(p)
ct = Thread(target=c.consume)

pt.start()
ct.start()


