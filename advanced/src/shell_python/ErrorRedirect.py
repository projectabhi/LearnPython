#This program stores stdout data into a file
import sys

#save stdout data
save_stdout = sys.stdout
fh = open("/root/Documents/python_project_files/stdout_test.txt","w")

sys.stdout = fh
sys.stdout.write("Writing through stdout statement\n")
print("Writing with print statement")

#Return to normal
sys.stdout = save_stdout

save_output = sys.stderr
fh = open("/root/Documents/python_project_files/error_test.txt","w")
sys.stderr = fh

x = 10/0

#Return to normal
sys.stderr = save_output

fh.close()