# Duck typing
class Speak:
    def callSpeak(obj):
        obj.speak()

class Human:
    def speak():
        print("Speaking")

class Cat:
    def speak():
        print("Meaowing")


Speak.callSpeak(Human)
Speak.callSpeak(Cat)

"""
    Here the same Speak class have taken multiple forms. As a Cat and Human. 
"""

# Dependency injection
class Flight:
    def __init__(self, engine) -> None:
        self.engine = engine # <- dependency injection, this class depends on an engine class

    def startEngine(self):
        self.engine.start()


class JetEngine:
    def start():
        print("Starting jet engine")

class ProperlerEngine:
    def start():
        print("Starting propeller engine")


plane1 = Flight(JetEngine)
plane1.startEngine()

plane2 = Flight(ProperlerEngine)
plane2.startEngine()