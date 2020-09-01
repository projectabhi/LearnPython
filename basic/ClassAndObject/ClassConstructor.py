class ComplexNumbers:

    #default constructor
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    #regular method using instance as argument
    def getdata(self):
        print("{0} + {1}".format(self.real, self.imag))

    # additional constructor
    @classmethod
    def from_str(cls,numberStr):
        real,imag,attr=numberStr.split('-')
        return cls(real,imag)

    # static method not using instance as argument
    @staticmethod
    def id_realnumber(number):
        if number%10 != 0:
            return False
        return True

c1 = ComplexNumbers(2,3)
c1.getdata()

c1 = ComplexNumbers.from_str('5-9-8')
c1.getdata()

print(c1.id_realnumber(10.05))

c2 = ComplexNumbers(5)
c2.attr = 10

print(c2.real,c2.imag,c2.attr)