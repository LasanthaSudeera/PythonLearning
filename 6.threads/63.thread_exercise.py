from threading import Thread


class EventNumber(Thread):
    def run(self) -> None:
        for i in range(1, 11):
            if i % 2 == 0:
                print(i)


class OddNumber(Thread):
    def run(self) -> None:
        for i in range(1, 11):
            if not i % 2 == 0:
                print(i)


en = EventNumber()
en.start()

on = OddNumber()
on.start()

for i in range(1, 101):
    print(i)
