mymixlist=['siva','sps','spspsp',9,2,4,6]
myintlist=[x for x in mymixlist if isinstance(x,int)]
mystrlist=[x for x in mymixlist if isinstance(x,str)]
print("My new list with int type: ",myintlist)
print("My new list with str type: ",mystrlist)