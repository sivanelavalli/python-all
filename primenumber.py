num=int(input("Enter a number: "))
k=0
for i in range(2,num//2+1):
  if(num%i==0):
     k=k+1
if(k<=0):
  print(num," is  prime number")
else:
  print(num, "is  not prime number")

