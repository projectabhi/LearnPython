'''
Created on 26-Aug-2018

@author: borokali
'''
import socket

s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('Got connection from:',addr)
    c.send('Thank you for connecting'.encode(encoding='utf_8', errors='strict'))
    c.close()
    