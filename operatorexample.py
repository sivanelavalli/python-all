class Book:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, other):
        x=self.name+other.name
        y=self.price+other.price
        print("Book name:",x)
        print("Book price:",y)
b1=Book('Core',1000)
b2=Book('Django',2000)
b1+b2
