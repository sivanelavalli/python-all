import random
print("Start the game")
while True:
    n=int(input("Enter the number between 1 to 10: "))
    i=random.randint(1,10)
    if(n!=i):
        print("Your number is: ",n)
        print("Random number is: ",i)
        print("Your guess is wrong")
        continue
    else:
        print("Your number is: ", n)
        print("Random number is: ", i)
        print("Your guess is right")
        break
print("you won the game")

