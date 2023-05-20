# Types of queues
import queue

# First in first out
q = queue.Queue()
q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(500)
while not q.empty():
    print(q.get(), end=" ")

print("\n")

# Last in first out
q = queue.LifoQueue()
q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(500)
while not q.empty():
    print(q.get(), end=" ")

print("\n")

# Priority queue (the given number is considered the priority)
q = queue.PriorityQueue()
q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(500)
while not q.empty():
    print(q.get(), end=" ")

print("\n")

# Non numeric data on a priprity queue, a tupple is is ued to give the priority
q = queue.PriorityQueue()
q.put((1, "Hello"))
q.put((10, "Love"))
q.put((2, " World"))
q.put((400, "Python"))
q.put((3, "I"))
while not q.empty():
    print(q.get()[1], end=" ")
