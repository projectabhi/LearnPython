'''
Created on 26-Aug-2018

@author: borokali
'''
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
print(s.recv(1024))
s.close()