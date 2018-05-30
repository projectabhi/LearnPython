'''
Created on 30-May-2018

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
