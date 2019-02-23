class Test:
    def fun1(self):
     n=int(input("Enter a number of elements to be inserted"))
     a=[]
     for i in range(0,n):
         e=int(input("Enter a number:"))
         a.append(e)
         avg=sum(a)/n
     print("The average of list is :",round(avg,2))
t=Test()
t.fun1()
