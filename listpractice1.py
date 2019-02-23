from functools import *
l=[5,11,9]
new=max(l)
l2=[new,new,new]
print(l2)
print("++++++++++++")
l=[2,3,4,5]
z=reduce(lambda x,y:x+y,l)
print(z)
print("------------------")
l=[[1,2,3],[4,5,6]]
l2=[l[0][1],l[1][1]]
print(l2)
