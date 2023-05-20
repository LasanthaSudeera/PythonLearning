"""
    Using multiple thread to improve the performace, by default eveything run on the main thread.

    Method One
    ----------

    Using a function

    t = Thread(target = functioName, args)
    t.start()

    Method Two
    -----------

    Extending the Thread class

    class MyThread(thread):
    
    overide the run() method

    then create a instance of this class and invoke it by t.start()

    Method Three
    -------------

    define a class, and pass an object from the instance

    class MyThread():
        display()

    t = Thread(taget = myobject.display, args)
"""

import threading

# Get the details on the current running thread
print(threading.current_thread().name)

# compare the thread
if threading.current_thread() == threading.main_thread() :
    print("Running on main thread")
else:
    print(threading.current_thread().name)

# Thread using a function
def printOneToTen():
    for i in range(1, 11):
        print(i)

    print("Running on print 1 to 10 thread ", threading.current_thread().name)

# Using a new thread with a function
t = threading.Thread(target=printOneToTen)
# invoking the function
t.start()

# Using a new thread by extending the Thread class
class newThread(threading.Thread):
    def run(self) -> None:
        for i in range(1, 11):
            print(i, threading.current_thread().name)
    
nt = newThread()
nt.start()

# Using a class

class ExamplePrint:
    def __init__(self, name) -> None:
        self.name = name

    def printName(self):
        for i in range(1,11):
            print(i, self.name, threading.current_thread().name)

ext = ExamplePrint("Jane Doe")
exttr = threading.Thread(target=ext.printName)
exttr.start()