num=int(input("Enter a number"))
count=0
while(num>0):
    dig=num%10
    count+=dig
    num=num//10
if count>=9:
    count=count-9
if count >= 9:
    count = count - 9
if count >= 9:
    count = count - 9
if count >= 9:
    count = count - 9
print(count)