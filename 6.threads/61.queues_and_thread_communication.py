"""
    The queue has two methods
        put()
        get()

    as the methods, the put() puts items to the queue, get() get the items to process
    put() will automotacally lock when peforming the put operation and get() will
    lock automatically as well


"""
from threading import *
from queue import Queue
import random
import time

def producer(queue:Queue):
    while True:
        print("Producing")
        queue.put(random.randint(1,50))
        print("Produced")
        time.sleep(2)

def consumer(queue:Queue):
    while True:
        print("Ready to consume")
        print("Consumed Data", queue.get())
        time.sleep(2)

queue = Queue()
t1 = Thread(target=producer, args=(queue,))
t2 = Thread(target=consumer, args=(queue,))
t1.start()
t2.start()