'''
Created on 01-Jun-2018
 In this section we will learn about python if .. else ...  statement.
@author: borokali
'''
today = "monday"

if today == "monday":
   print("this is monday")
elif today == "tuesday":
   print("this is tuesday")
elif today == "wednesday":
   print("this is wednesday")
elif today == "thursday":
   print("this is thursday")
elif today == "friday":
   print("this is friday")
elif today == "saturday":
   print("this is saturday")
elif today == "sunday":
   print("this is sunday")
else:
   print("something else")
   
 ####################################################
 
today1 = "holiday"
bank_balance = 20000
if today1 == "holiday":
   if bank_balance > 20000:
      print("Go for shopping")
   else:
      print("Watch TV")
else:
   print("normal working day")  