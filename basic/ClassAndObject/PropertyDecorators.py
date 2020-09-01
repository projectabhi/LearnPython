class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    @fullname.setter
    def fullname(self,name):
        fname,lname=name.split(' ')
        self.fname=fname
        self.lname=lname

    def __repr__(self):
        return 'Employe-FirstName:{},LastName:{},Fullname:{}'.format(self.fname,self.lname,self.fullname)

emp1=Employee('Test1','User1')
emp2=Employee('Test2','User2')

print(emp1)
emp2.fullname='Test User'
print(emp2)