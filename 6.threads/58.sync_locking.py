import threading

class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        # self.l = threading.Lock() # Initiating the locking
        self.l = threading.Semaphore() # Using a Semaphore instaed of the lock.

    def buy(self, seatAmount):
        print("Total seats available", self.availableSeats)
        self.l.acquire() # Adding the lock

        if(self.availableSeats >= seatAmount):
            self.availableSeats -= seatAmount
            print("Reserving seats")
            print("Processing payment")
            print("Printing receipt")
        else:
            print("Seats unavailable")

        self.l.release() # releasing the lock

obj = BookMyBus(10)
t1 = threading.Thread(target=obj.buy, args=(5,))
t2 = threading.Thread(target=obj.buy, args=(2,))
t3 = threading.Thread(target=obj.buy, args=(4,))

t1.start()
t2.start()
t3.start()