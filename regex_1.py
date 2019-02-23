import re
pattern="^a...s$"
lst1=['asivs','adsds','aaaaa','asas','asdgs']
lst2=[]
for x in lst1:
 result=re.match(pattern,x)
 if result:
    lst2.append(x)
    print(lst2)
 else:
    print("this is not "+x+"  as per our requirement")