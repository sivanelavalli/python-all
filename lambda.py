from functools import *
numbers=range(10)
new_list=[]
x=[lambda n:n**2 for n in numbers if n%2==0]
new_list.append(x)
print(new_list)