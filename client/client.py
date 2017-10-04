#!/usr/bin/env python
# coding: utf-8

import socket

hote="192.168.0.223"
port = 25500

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.sendto("Salut",(hote,port))

socket.close
