#!/usr/bin/env python
#coding: utf-8

import Tkinter as tk
from VoilierClient import *


class IHM(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.objetVoilier=VoilierClient()
        self.grid()
        self.titre = tk.Label(self, text="Interface de test du Voilier")
        self.titre.pack()
        
        #LABELS
        self.lbIP = tk.Label(self, text="IP :")
        self.lbPort = tk.Label(self, text="Port")
        self.lbGV = tk.Label(self, text="GV")
        self.lbSafran = tk.Label(self, text="Safran")
        self.lbGite = tk.Label(self, text="Gite :")
        self.lbLatitude = tk.Label(self, text="Latitude :")
        self.lbLongitude = tk.Label(self, text="Longitude :")
        self.lbVitVent = tk.Label(self, text="Vitesse vent :")
        self.lbOrientVent = tk.Label(self, text="Orientation vent :")

        #CONTROLES
        self.lbGiteValue = tk.Label(self, text="0")
        self.lbLatitudeValue = tk.Label(self, text="0")
        self.lbLongitudeValue = tk.Label(self, text="0")
        self.lbVitVentValue = tk.Label(self, text="0")
        self.lbOrientVentValue = tk.Label(self, text="0")
        self.inputIP = tk.Entry(self, width=15)
        self.inputIP.insert(0,"127.0.0.1")
        self.inputPort = tk.Entry(self, width=5)
        self.inputPort.insert(0,"25500")
        self.boutonConnect = tk.Button(self, text="Connect",command=self.connect)
        self.scaleGV = tk.Scale(self, orient=tk.HORIZONTAL, from_=0,to=180,command=self.valueGVChanged)
        self.scaleSafran = tk.Scale(self, orient=tk.HORIZONTAL, from_=0,to=180,command=self.valueSFChanged)
        self.log=tk.Text(self,height=5,bg='black',fg='white')
        self.bouton_test=tk.Button(self, text="tester",command=self.test)

        #POSITIONNEMENT
        self.titre.grid(row=0,column=0,columnspan=5)

        self.lbIP.grid(row=1, column=0, pady=30)
        self.inputIP.grid(row=1,column=1)
        self.lbPort.grid(row=1,column=2)
        self.inputPort.grid(row=1,column=3,sticky=tk.W)
        self.boutonConnect.grid(row=1,column=4)

        self.lbGV.grid(row=3,column=0,columnspan=2)
        self.scaleGV.grid(row=4,column=0,columnspan=2)

        self.lbSafran.grid(row=5,column=0,columnspan=2)
        self.scaleSafran.grid(row=6,column=0,columnspan=2)
        self.bouton_test.grid(row=6,column=2,columnspan=1)

        self.lbGite.grid(row=3,column=3,sticky=tk.E)
        self.lbVitVent.grid(row=4,column=3,sticky=tk.E)
        self.lbOrientVent.grid(row=5,column=3,sticky=tk.E)
        self.lbLatitude.grid(row=6,column=3,sticky=tk.E)
        self.lbLongitude.grid(row=7,column=3,sticky=tk.E)

        self.lbGiteValue.grid(row=3,column=4,sticky=tk.W)
        self.lbVitVentValue.grid(row=4,column=4,sticky=tk.W)
        self.lbOrientVentValue.grid(row=5,column=4,sticky=tk.W)
        self.lbLatitudeValue.grid(row=6,column=4,sticky=tk.W)
        self.lbLongitudeValue.grid(row=7,column=4,sticky=tk.W)

        self.log.grid(row=8,column=0,columnspan=5)


    def connect(self):
        self.log.insert('1.0',"Connection...\n")
        self.objetVoilier.initCom(self.inputIP.get(),int(self.inputPort.get()))
        self.log.insert('1.0',self.inputPort.get())
        self.log.insert('1.0',"Port du serveur: ")
        self.log.insert('1.0',self.inputIP.get())
        self.log.insert('1.0',"Adresse du serveur: ")

    def test(self):
        self.objetVoilier.txrx(self.scaleSafran.get(),self.scaleGV.get())
        self.lbGiteValue.config(text=self.objetVoilier.gite)
        self.lbLatitudeValue.config(text=self.objetVoilier.latitude)
        self.lbLongitudeValue.config(text=self.objetVoilier.longitude)
        self.lbVitVentValue.config(text=self.objetVoilier.vVent)
        self.lbOrientVentValue.config(text=self.objetVoilier.orientationVent)



    def valueGVChanged(self,value):
        s=str("GV=")+value+"\n"
        self.log.insert('1.0',s)

    def valueSFChanged(self,value):
        s=str("SF=")+value+"\n"
        self.log.insert('1.0',s)

monIHM=IHM()
monIHM.mainloop()