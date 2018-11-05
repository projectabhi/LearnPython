# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


def custom_factorial(x):
    if x == 0:
        return 1
    return x * custom_factorial(x - 1)


a = int(input("Enter the number for factorial:"))
print(custom_factorial(a))
