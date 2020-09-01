class Employee:
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay

    def __repr__(self):
        return '{}-{}'.format(self.fullname(), self.pay)

    def __str__(self):
        return 'Employee({},{},{})'.format(self.fname, self.lname, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def fullname(self):
        return self.fname+' '+self.lname

    def raisePay(self,tax):
        self.pay = int(self.pay)+ int(tax)

    @classmethod
    def from_string(cls,csvString):
        fname,lname,pay=csvString.split(',')
        return cls(fname,lname,pay)

    @staticmethod
    def lengthOfFullname(fullname):
        return len(fullname)

emp1=Employee('Abhijit','Dey',12000)
emp2=Employee('Test','User',13000)
emp3=Employee.from_string('Test2,User2,14000')
emp3.raisePay(1200)
print(emp1.fname)
print(emp2.fname)

print(emp1.fullname())
print(emp1.lengthOfFullname(emp1.fullname()))
print('Employee Name: {} , rate: {}'.format(emp3.fullname(),emp3.pay))
#start: calling magic methods
print(emp1)
print(emp1+emp2)
#end: calling magic methods