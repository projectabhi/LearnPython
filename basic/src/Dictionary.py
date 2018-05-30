'''
Created on 30-May-2018
Dictionary is a python data type that is used to store key value pairs.
It enables you to quickly retrieve, add, remove, modify, values using key. 
Dictionary is very similar to what we call as Map in java
@author: borokali
'''
friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111',
'nibble':'222-333-444'
}

print(friends)
print(friends['tom'])

del friends['nibble']
print(friends)

for key in friends:
    print(key,":",friends[key])
    
print(len(friends))
