'''
Created on 01-Jun-2018
Functions are the re-usable pieces of code which helps us to organize structure 
of the code. We create functions so that we can run a set of statements multiple 
times during in the program without repeating ourselves.
@author: borokali
'''
def sum(start,end):
    result=0
    for i in range(start,end+1):
        result +=i
    print(result)
    
sum(1,5)
#####################################
def sum2(start, end):
   result = 0
   for i in range(start, end + 1):
       result += i
   return result

s = sum2(10, 50)
print(s)
###################################
def sum3(start, end):
   if(start > end):
       print("start should be less than end")
       return    # here we are not returning any value so a special value None is returned
   result = 0
   for i in range(start, end + 1):
       result += i
   return result

s = sum3(110, 50)
print(s)
########### GLOBAL VARIABLE #############
global_var = 12         # a global variable

def func():
    local_var = 100     # this is local variable
    print(global_var)   # you can access global variables in side function

func()                  # calling function func()

#print(local_var)        # you can't access local_var outside the function, because as soon as function ends local_var is destroyed
########### GLOBAL VARIABLE 2 #############
xy = 100

def cool():
    xy = 200     # xy inside the function is totally different from xy outside the function
    print(xy)    # this will print local xy variable i.e 200

cool()

print(xy)        # this will print global xy variable i.e 100

########### GLOBAL VARIABLE 3 #############
t = 1

def increment():
    global t   # now t inside the function is same as t outside the function
    t = t + 1
    print(t) # Displays 2


increment()
print(t) # Displays 2

########## Returning multiple values from function #######
def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

s = bigger(12, 100)
print(s)
print(type(s))
