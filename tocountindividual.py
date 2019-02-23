first=12453
last=12462
sum = 0
for i in range(first,last):
    temp = i
    while i >0:
      rem = i % 10
      sum += rem
      i //= 10
    print("Sum of all digits",temp ,"is",sum)
