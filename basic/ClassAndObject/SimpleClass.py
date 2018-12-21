class SimpleClass:
    "This is my class"
    a = 10
    def func(self):
        print("Hello")


print(SimpleClass.a)

print(SimpleClass.func)

SimpleClass.func(' ')

print(SimpleClass.__doc__)