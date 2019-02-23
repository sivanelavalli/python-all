class Item:
    def __init__(self,id,name,price):
        self.itemid=id
        self.itemname=name
        self.price=price
    def __str__(self):
        return 'itemid={},itemname={},price={}'.format(self.itemid,self.itemname,self.price)
pobj=Item(101,'samsung',15000)