class TooManyValuesException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class Test:
    def show(self,mylist):
        try:
         if len(mylist)>5:
            raise TooManyValuesException("List has more than 5 elements")
        except TooManyValuesException as tm:
            print(tm)
        else:
            print("List is accepted")
            print("The list is:",mylist)
#calling block
t=Test()
lst=[1,3,5,7]
t.show(lst)



