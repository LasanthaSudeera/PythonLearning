class Car:

    # Constructer
    def __init__(self, make:str, year:str):
        self.make = make
        self.year = year

    # Inner Class
    class Engine:
        # Constructer for the inner class
        def __init__(self, number:int):
            self.number = number
        
        def getEngineNumber(self):
            return self.number


# Creating a object Car
car = Car('Toyota', 1994)
print(car.make, car.year)
# Creating an inner object
engine = car.Engine(123)
print(engine.getEngineNumber())


        