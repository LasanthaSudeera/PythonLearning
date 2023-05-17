class BMW:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Car starting")

class Series3(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year) -> None:
        BMW.__init__(self, make, model, year) # Using the parent class as BMW.
        self.cruiseControlEnabled = cruiseControlEnabled
    
    # Overridding parent methods
    def start(self):
        print("Button Start")

class Series2(BMW):
    def __init__(self, parkingAssisantEnabled, make, model, year) -> None:
        super().__init__(make, model, year) # Using the super() to reffer to the parent class
        self.parkingAssistantEnabled = parkingAssisantEnabled

car = Series2(True, "Make", "Model", 1994)
print(car.parkingAssistantEnabled)
print(car.model)
print(car.make)
car.start()

car2 = Series3(False, "Beta", "Modelz", 1986)
print(car2.cruiseControlEnabled)
print(car2.model)
print(car2.make)
car2.start()