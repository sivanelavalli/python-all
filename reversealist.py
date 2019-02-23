lst=[1,2,3,4,5]
#first way using reverse() function
lst.reverse()
print(lst)
print("==========")
#second way using Slicing
#syntax[start:end:step]
newlst=lst[::-1]
print(newlst)
print("==============")
#third using reversed() built-in function
lst1=[[1,2],[3,4],[5,6],[7,8]]
y=[]
for x in reversed(lst1):
    x.reverse()
    y.append(x)
    print(y)