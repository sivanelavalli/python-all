class Book:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, other):
        x=self.name+other.name
        y=self.price+other.price
        print("Book name:",x)
        print("Book price:",y)
b1=Book('core',1000)
b2=Book('python',2000)
b3=Book('django',3000)
b4=b1+b2
b5=b4+b3
print("Book name=",b5.name)
print("Book price=",b5.price)