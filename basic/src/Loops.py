'''
Created on 01-Jun-2018
python has only two loops for and  while 
@author: borokali
'''
my_list = [1,2,3,4]

for i in my_list:
    print(i)
print("----------------------")   
############ RANGE with step ###############

for i in range(1, 20, 2):
    print(i)
print("----------------------")       
############WHILE with BREAK #############
count = 0

while count < 10:
    count += 1
    if count == 5:
         break    
    print("inside loop", count)
print("out of while loop")
############WHILE with Continue #############
count2 = 0

while count2 < 10:
    count2 += 1
    if count2 % 2 == 0:
           continue
    print(count2)
