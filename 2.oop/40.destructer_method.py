class Product:
    
    # __init__ is the constructer
    def __init__(self):
        self.name = "Iphone"
        self.price = "Too much"
        self.desc = "Waste of money"

    """
        __del__ can be useful to destroy an instance when the job is done. Example a connection to database
        can be closed after the functionality is served.
    """
    def __del__(self):
        print("Inside the destructer")
        
p1 = Product()
print(p1.name)
p1 = None

p2 = Product()
print(p2.price)
p2 = None