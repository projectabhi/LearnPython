'''
Created on 30-May-2018

@author: borokali
'''
list1=[1,2,3,4]
list2=["String",12]

print(list1)
print(list2)

#Other ways to create list
list3 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list4 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list5 = list("python") # Create a list with characters p, y, t, h, o, n

print(list3[1])
print(22 in list3)

list6=list3+list4
print(list6)

print(len(list6)) # find the number of elements in the list
print(max(list3)) # find the largest element in the list
print(min(list3)) # find the smallest element in the list
print(sum(list1)) # sum of elements in the list

#List slicing
origList=list([1,2,3,4,22, 31, 61])
print("index 0 to 4:"+str(origList[0:5]))
print("index 0 to 4:"+str(origList[:5]))
print("index 2 to end:"+str(origList[2:]))

# * operator replicates the elements in the list.
origList1= origList*2
print(origList1)

#Adds an element x to the end of the list and returns None.
origList.append(100)
print(origList)

#Returns the number of times element x appears in the list.
print("Count of 22 in origList1:"+str(origList1.count(22)))

#Appends all the elements in list3  to the list and returns None.
list1.extend(list3)
print("list1 extended"+str(list1))

list1.insert(2, 100)
print(list1)

list1.remove(31)
print(list1)

list1.reverse()
print(list1)

list1.sort(key=None, reverse=False)
print(list1)

list1.pop(2)
print(list1)

comprehensiveList=[x for x in range(10)]
print(comprehensiveList)

comprehensiveList2=[x*2 for x in range(10) if x%2==0]
print(comprehensiveList2)
