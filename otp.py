import string,random
def generatepassword():
    password=''
    for n in range(16):
        x=random.randint(0,94)
        password+=string.printable[x]
    return password
print(generatepassword())