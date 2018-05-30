'''
Created on 31-May-2018
Tuples are very similar to list 
but once a tuple is created, you cannot add, delete, replace, reorder elements.
@author: borokali
'''
t1 = () # creates an empty tuple with no data
t2 = (11,22,33)
t3 = tuple([1,2,3,4,4]) # tuple from array
t4 = tuple("abc") # tuple from string

print("Min of t2",min(t2))
print("Max of t3", max(t3))
print("Sum of t2",sum(t2))
print("length of string tuple:",len(t4))

print("does d exist in string tuple t4:", "d" in t4)

for i in t2:
    print(i,end=" ")