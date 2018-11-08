import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if(i == 0):
        print("Function Name:" + sys.argv[0])
    else:
        print("Argument:" + (i, sys.argv[i]))
