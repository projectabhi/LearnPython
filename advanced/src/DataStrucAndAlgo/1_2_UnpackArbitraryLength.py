# Star expression to unpack N elements from large iterable
def avg(numbers):
    return sum(numbers)/len(numbers)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

data = [12.00, 13.00, 14.00, 15.00, 16.50, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00]
result = drop_first_last(data)
print(round(result, 2))
