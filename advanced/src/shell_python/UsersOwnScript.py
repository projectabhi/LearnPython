import os

command = ""
while(command != "exit"):
    command = input("borokali's prompt:")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print(line)
    handle.close()

print("Hope you liked it")