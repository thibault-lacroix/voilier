#!/usr/bin/env python
# coding: utf-8

import socket

hote='127.0.0.1'
port=25500

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Demarage du server"

socket.bind((hote,port))

latitude=-5689521
b3=(latitude>>24)&0xFF
b2=(latitude>>16)&0xFF
b1=(latitude>>8)&0xFF
b0=latitude&0xFF

longitude=4541237
b7=(longitude>>24)&0xFF
b6=(longitude>>16)&0xFF
b5=(longitude>>8)&0xFF
b4=longitude&0xFF

gi=30 #gite

dv=230 #direction du vent

vv=10 #vitesse du vent



while True:
    data,addr=socket.recvfrom(1024)
    print "message recu:"
    print "id: ",ord(data[0])
    print "taille: ",ord(data[1])
    print "safran: ",ord(data[2])
    print "GV: ",ord(data[3])
    trameReponse=bytearray([b0,b1,b2,b3,b4,b5,b6,b7,gi,dv,vv])
    socket.sendto(trameReponse,(addr))

#print "fermeture"
#client.close()
#socket.close()
