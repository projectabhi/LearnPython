### Unpacking a tuple of sequence into separate variables
p = (4, 5)
x, y = p
print(x)
print(y)

### Array Unpacking ###
data = ['ACME', 50, 91.1, (2018, 11, 25)]
name, shares, price, date = data
print("Name:", name, "~~Shares:", shares, "~~Price:", price, "~~Date:", date)

name2, shares2, price2, (year, mon, day) = data
print("Name2:", name2, "~~Shares2:", shares2, "~~Price2:", price2, "~~Day:", day, "~~Month:", mon, "~~Year:", year)

### Discarding some elemets from data array ###
_, shares3, price3, _ = data
print("~~Shares3:", shares3, "~~Price3:", price3)

### Unpacking Strings ###
s = "Hello"
a,b,c,d,e = s
print(a, "~",b ,"~" ,c , "~",d , "~", e)
