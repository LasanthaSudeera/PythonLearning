# Private variables
class Student:
    def __init__(self) -> None:
        """
            __variableName is the way a private variable is defined. Outside of this class,
            they are not accessible. Getters and setters should be defined in order to manipulate them
        """
        self.__name = "John Doe"
        self.__age = 29

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


s = Student()
print(s.getName())
s.setName("Jane Doe")
print(s.getName())

"""
    In python when a variable is defined private, it not completely hidden, it can be accessed as below

    syntax: obj._ClassName__variableName
"""

print(s._Student__name)

# Exercise
class Patient:
    def __init__(self) -> None:
        self.__id = None
        self.__name = None
        self.__ssn = None

    def setId(self, id: int):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name: int):
        self.__name = name

    def getName(self):
        return self.__name

    def setSSN(self, ssn: int):
        self.__ssn = ssn

    def getSSN(self):
        return self.__ssn

p1 = Patient()
p1.setId(1)
p1.setName("John Doe")
p1.setSSN("RND123")

print(p1.getId())
print(p1.getName())
print(p1.getSSN())
