from functools import reduce

class Course:
    # Global static variables
    major = "Courses"

    # Constructer
    def __init__(self,name: str,ratings: list):
        self.name=name
        self.ratings=ratings
        self.author=None

    def getAvgRating(self):
        return reduce(lambda x,y: (x+y), self.ratings) /(len(self.ratings)+1)
    
    def getName(self):
        return self.name
    
    def setName(self,name:str):
        self.name = name

    def setAuthor(self, author:str):
        self.author = author

    def getAuthor(self):
        return self.author


a = Course("C# Course", [5,4])
a.setName("Python Course")
print(a.getAvgRating(), a.getName(), a.getAuthor())

b = Course("Java Couse", [10,10,5])
b.setAuthor("Lasantha Sanjeewa")
print(b.getAvgRating(), b.getName(), b.getAuthor(), b.major)

# You can access the global static variables without creating and instantiating a new class
print(Course.major)