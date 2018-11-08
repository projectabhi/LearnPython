import sys

print("Coming through stdout")

# stdout is saved
save_stdout = sys.stdout

fh = open("/root/Documents/python_project_files/test.txt", "w")

sys.stdout = fh
print("This line goes to test.txt\n")
print("Adding another line")
# return to normal:
sys.stdout = save_stdout

fh.close()