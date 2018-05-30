'''
Created on 29-May-2018
Opening a file and perform read and write operation./media/borokali/IMP/pythonRead
towrite first and then read the same
@author: borokali
'''
from past.builtins.misc import raw_input
#First write a file
f_path=raw_input("Enter the path:")
f_name=raw_input("Enter the filenName:")
fileNameWithPath=f_path+"/"+f_name
print(fileNameWithPath)
fileToWrite=open(fileNameWithPath,"w")
fileToWrite.write("Hello world \n")
fileToWrite.write("Line no 2 \n")
fileToWrite.write("Line no 3")
fileToWrite.close()

fileRead=raw_input("Enter a file name to read:") 
fullReadPath=f_path+"/"+fileRead
fo=open(fullReadPath, "r")
for line in fo:
    print(line)
    
fo.close()