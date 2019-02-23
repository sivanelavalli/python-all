class Phone:
    def __init__(self,brand,price,battery):
        self.brand=brand
        self.price=price
        self.battery=battery
    def buy(self):
        print("buying the mobile")
    def exchange(self):
        print("exchanging the phone")
class FeaturedPhone(Phone):
    def __init__(self,brand,price,battery):
        super().__init__(brand,price,battery)
    def returns(self):
        print("Phone is returned")
class SmartPhone(Phone):
    def __init__(self,brand,price,battery,ram,camera):
        self.ram=ram
        self.camera=camera
        super().__init__(brand,price,battery)
    def insurance(self):
        print("The phone is insured")
#calling block
b=input("Enter the brand name")
p=input("Enter the price")
y=input("Enter the battery capacity")
f=FeaturedPhone(brand=b,price=p,battery=y)
result=f.buy()
print(result)
sm=SmartPhone(brand=b,price=p,battery=y,ram='4gb',camera='24mp')
result1=sm.exchange()
print(result1)