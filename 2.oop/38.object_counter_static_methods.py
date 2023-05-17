class ObjectCounter:

    numberOfObjects = 0
    # Constructer
    def __init__(self):
        # Increase the globally defined numberOfObjects when a new instance is created
        ObjectCounter.numberOfObjects += 1

    # Creating a static method by using the decorator @staticmethod
    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

a = ObjectCounter()
b = ObjectCounter()
print(ObjectCounter.numberOfObjects)

# Invoking the static method
ObjectCounter.displayCount()