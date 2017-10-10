#!/usr/bin/env python
# coding: utf-8

import socket

hote="192.168.0.223"
port = 25500

trame = bytearray([25,12,1,30])

print "UDP target IP: ",hote
print "UDP target port: ",port

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.sendto(trame,(hote,port))
print "message envoyé:", trame[0],trame[1],trame[2],trame[3]


trameReponse,addr=socket.recvfrom(1024)
#print "message recu: ",ord(data[0]),ord(data[1]),ord (data[2]),ord(data[3])
#print "id: ",ord(data[0])
#print "taille: ",ord(data[1])
#print "safran: ",ord (data[2])
#print "GV: ",ord(data[3])
print "latitude: ",ord(trameReponse[0]),ord(trameReponse[1]),ord(trameReponse[2]),ord(trameReponse[3])




#socket.close
