from abc import abstractmethod, ABC

# Abstract class
class BMW(ABC): # Inheriting from the ABC modules make the followng classes to make abstract methods mandatary
    @abstractmethod
    def drive():
        pass

class TwoSeries(BMW):
    def color(self):
        return "Red"
    
    def drive(self):
        return "Driving"

car = TwoSeries()
print(car.color())
print(car.drive())

# Sample interface, interface is a class with nothing but only abstract methods
class SampleInterface(ABC):

    @abstractmethod
    def requiredMethod():
        pass

    @abstractmethod
    def requiredMethodsTwo():
        pass

class ConcreteClass(SampleInterface):
    def privateMethod():
        return "Oka"
    
    def requiredMethod(self):
        return "mt 1"
    
    def requiredMethodsTwo():
        return "mt 2"
    

cc = ConcreteClass()
print(cc.requiredMethod())

# Exercise

class TouchScreenLaptop(ABC):

    @abstractmethod
    def click():
        pass

    @abstractmethod
    def scroll():
        pass


class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scroll")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Dell Scroll")

class HPNoteBook(HP):
    def click(self):
        print("HP Click")

class DellNotebook(Dell):
    def click(self):
        print("Dell Click")


dellLap = DellNotebook()
dellLap.click()
dellLap.scroll()

HpLap = HPNoteBook()
HpLap.click()
HpLap.scroll()