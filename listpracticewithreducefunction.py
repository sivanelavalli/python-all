from functools import *
l=[1,2,3]
l1=reduce(lambda x,y:x+y,l)
print(l1)