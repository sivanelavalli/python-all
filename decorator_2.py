def deco(func):
    def wrap():
        service_tax=0.5
        return service_tax*func()/10+func()
    return wrap
@deco
def new():
    shoes=40
    clothes=40
    result=shoes*2
    return result
print(new())
@deco
def new1():
    mobile=8000
    result=mobile*5
    return result
print(new1())
print("----------------------------------")
def strong(func):
    def wrapper():
        a=5
        return a+ func()
    return wrapper
def emphasis(func):
    def wrapper():
        b=6
        return b+ func()
    return wrapper
@strong
@emphasis
def greet():
    c=4
    d=7
    result=c+d
    return result
print(greet())
