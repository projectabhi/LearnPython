class ComplexNumbers:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def getdata(self):
        print("{0} + {1}j".format(self.real, self.imag))

c1 = ComplexNumbers(2, 3)

c1.getdata()

c2 = ComplexNumbers(5)
c2.attr = 10

print(c2.real,c2.imag,c2.attr)