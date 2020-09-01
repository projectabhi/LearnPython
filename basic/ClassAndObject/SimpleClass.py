from basic.ClassAndObject import ClassConstructor
class SimpleClass:
    "This is my class"
    a = 10
    def __init__(self):
        self.a=11

    def func(self):
        print("Hello")

s=SimpleClass()
print(SimpleClass.a)
print(s.a)
print(SimpleClass.func)

SimpleClass.func(' ')

print(SimpleClass.__doc__)
c1=ClassConstructor.ComplexNumbers()
print(c1.is_realnumber(100))