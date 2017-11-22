#!/usr/bin/env python
# coding: utf-8

import socket

class VoilierClient:

	def __init__(self):	# Contructeur, valeurs par defaut
		self.ip=""
		self.port=25500
		self.valSF=0
		self.valGV=0
		self.gite=0
		self.latitude=0
		self.longitude=0
		self.vVent=0
		self.orientationVent=0
		self.id=0


	def initCom(self, ip, port):# Def port et ip du serveur
		self.ipserv=ip
		self.portserv=port
		self.socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Creation de la socket


	def txrx(self,valGV,valSF):
		
		self.valGV=valGV
		self.valSF=valSF


		trame = bytearray([self.id,2,valSF,valGV]) # Definition de la trame
		self.socket.sendto(trame,(self.ip,self.port)) # Envoi la trame au serveur avec l'ip et le port
		self.id+=1	# id incrementation de 1 a chaque envoi d'une trame
		print "message envoyé:", trame[0],trame[1],trame[2],trame[3] # Affiche la trame envoyée

		trameReponse,addr=self.socket.recvfrom(1024) # trameReponse contient les données reçus depuis le serveur avec un buffer d'une taille de 1024
		latitude1=(ord(trameReponse[3])<<24)|(ord(trameReponse[2])<<16)|(ord(trameReponse[1])<<8)|ord(trameReponse[0]) 	# Latitude avec le decalage de bit
		longitude1=(ord(trameReponse[7])<<24)+(ord(trameReponse[6])<<16)+(ord(trameReponse[5])<<8)+ord(trameReponse[4]) # Longitude avec decalage de bit

		self.gite=ord(trameReponse[8]) # La gite se trouve dans l'octet 8
		self.orientationVent=ord(trameReponse[9]) # L'orientation du vent se trouve dans l'octet 9
		self.vVent=ord(trameReponse[10]) # La vitesse du vent se trouve dans l'octet

		b7=ord(trameReponse[7])
		b3=ord(trameReponse[3])

		if b3>127:									#
			latitude1=(~latitude1)&0xFFFFFFFF		#
			latitude1=latitude1+1					#
			latitude1=latitude1*-1					#
													#
													# Passe les nombres binaires en negatifs	
		if b7>127:									#
			longitude1=(~longitude1)&0xFFFFFFFF		#	
			longitude1=longitude1+1					#
			longitude1=longitude1*-1				#


		self.latitude=float(latitude1)/1000000		#
		self.longitude=float(longitude1)/1000000	# Division par 1000000 pour retrouver le nombre initial


#objetVoilier=VoilierClient() # Nom de l'objet 
#objetVoilier.initCom("127.0.0.1",25500) # Definition d'une IP et d'un port
#objetVoilier.valSF=12 # Valeur du safran
#objetVoilier.valGV=56 # Valeur de la grand voile
#objetVoilier.txrx()
#print "Latitude :",objetVoilier.latitude 				    #
#print "Longitude :",objetVoilier.longitude 	 			#
#print "Gite :",objetVoilier.gite  						    # Affichage
#print "Vitesse du vent: ",objetVoilier.vVent			    #
#print "Orientation du vent: ",objetVoilier.orientationVent #			