class Computer:

    def __init__(self):
        self.__maxprice = 600

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1200
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()