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