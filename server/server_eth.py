#!/usr/bin/env python
# coding: utf-8

import socket

hote='192.168.0.223'
port=25500

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Demarage du server"

socket.bind((hote,port))

latitude=1651782
b3=(latitude>>24)&0xFF
b2=(latitude>>16)&0xFF
b1=(latitude>>8)&0xFF
b0=latitude&0xFF
print hex(b3)
print hex(b2)
print hex(b1)
print hex(b0)

while True:
    data,addr=socket.recvfrom(1024)
    print "message recu:"
    print "id: ",ord(data[0])
    print "taille: ",ord(data[1])
    print "safran: ",ord(data[2])
    print "GV: ",ord(data[3])
    trameReponse=bytearray([b0,b1,b2,b3,data[1]])
    socket.sendto(trameReponse,(addr))


#print "fermeture"
#client.close()
#socket.close()


