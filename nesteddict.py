mydict= {'x': {'items':['a','b','c']},'y': {'items':['d','e','f']},'z':{'items':['a','b','c']}}
for v in mydict.values():
    for c in v.values():
        for i in c:
            print(i,end="")
            print()
