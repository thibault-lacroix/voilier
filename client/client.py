#!/usr/bin/env python
# coding: utf-8

import socket

hote="127.0.0.1"
port = 25500

trame = bytearray([25,12,1,30])
print "   "
print "UDP target IP: ",hote
print "UDP target port: ",port

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.sendto(trame,(hote,port))
print "message envoyé:", trame[0],trame[1],trame[2],trame[3]
print "       "


trameReponse,addr=socket.recvfrom(1024)

latitude1=(ord(trameReponse[3])<<24)|(ord(trameReponse[2])<<16)|(ord(trameReponse[1])<<8)|ord(trameReponse[0])
longitude1=(ord(trameReponse[7])<<24)+(ord(trameReponse[6])<<16)+(ord(trameReponse[5])<<8)+ord(trameReponse[4])
b7=ord(trameReponse[7])
b3=ord(trameReponse[3])
gite=ord(trameReponse[8])
dirVent=ord(trameReponse[9])
vitVent=ord(trameReponse[10])


if b3>127:
	latitude1=(~latitude1)&0xFFFFFFFF
	latitude1=latitude1+1
	latitude1=latitude1*-1



if b7>127:
	longitude1=(~longitude1)&0xFFFFFFFF
	longitude1=longitude1+1
	longitude1=longitude1*-1



print "Reponse du serveur: "
print "         "
print "latitude: ",float(latitude1)/1000000
print "longitude: ",float(longitude1)/1000000
print "Gite: ",gite,"°"
print "Direction du vent: ",dirVent,"°"
print "Vitesse du vent: ",vitVent,"nd"

#socket.close