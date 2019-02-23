import time
import math
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+" took : "+str((end-start)))
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
        return result
    print(result)

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
        return result
    print(result)
array=range(1,50000)
count_cube=calc_cube(array)
count_square=calc_square(array)