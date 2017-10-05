#!/usr/bin/env python
# coding: utf-8

import socket

hote='192.168.0.223'
port=25500

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Demarage du server"

socket.bind((hote,port))

while True:
    data,addr=socket.recvfrom(1024)
    print "message recu:"
    print "id: ",ord(data[0])
    print "taille: ",ord(data[1])
    print "safran: ",ord(data[2])
    print "GV: ",ord(data[3])
    socket.sendto(data,(addr))


#print "fermeture"
#client.close()
#socket.close()


