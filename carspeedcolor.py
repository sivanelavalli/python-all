class car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed=speed
        self.color=color
        print("the __init__ is called")
nissan=car(100,'teerblue')
swift=car(120,'white')

print(nissan.speed)
print(swift.color)
