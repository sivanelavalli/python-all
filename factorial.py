n=int(input("Enter a no: "))
factorial=1
sum=1
while sum<=n:
    factorial=factorial*sum
    sum=sum+1
    print("The factorial of",n,"is: ",factorial)