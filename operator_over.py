class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal
    def __lt__(self, other):
        if self.salary<other.salary:
            return True
        else:
            return False
e1=Employee('siva',20000)
e2=Employee('prasad',50000)
if e1<e2:
    print(e1.name,'salary is greater than',e2.name)
else:
    print(e1.name, 'salary is not greater than', e2.name)