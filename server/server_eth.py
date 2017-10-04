#!/usr/bin/env python
# coding: utf-8

import socket

hote='192.168.0.223'
port=25500

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Demarage du server"
socket.bind((hote,port))

while True:
    data,addr=socket.recvfrom(6)
    print data

#print "fermeture"
#client.close()
#socket.close()
    


