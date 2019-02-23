import itertools
lst1=[1,2,3]
lst2=[4,5,6]
for item in itertools.chain(lst1,lst2):
 #without using + operator add two lists
 lst3=[*lst1,*lst2]
 print(lst3)