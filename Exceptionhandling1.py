class AmountOverflowException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class InvaliAmountException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class Bank:
    def __init__(self,balance):
        self.bal=balance
    def withdraw(self,amount):
        try:
            if(amount>20000):
                raise AmountOverflowException("Amount is exceeded limit is 20000 only")
            else:
                self.bal-=amount
                if self.bal<1000:
                    raise InvaliAmountException("you can't withdraw")
                print("Remaining balance after withdraw:",self.bal)
        except AmountOverflowException as e:
            print(e)
        except InvaliAmountException as ie:
            print(ie)
#calling block
bk=Bank(balance=20000)
bk.withdraw(19000)
