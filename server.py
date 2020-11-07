import socket
import sys
import time
from check import ip_checksum
import random

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))

windowSize = 3

print "Created Socket and bind"

expecting=0
while 1:
	d = s.recvfrom(1024)
	data=d[0]
	addr=d[1]
	seq=data[0]
	msg=data[2:12]
	checksum=data[12:]
	checksum2=ip_checksum(msg)
	print seq, '-', msg, ' ,checkusm = ', checksum,' from ',addr
	
	if not d:
		break

		s.sendto('ACK for '+d[0], d[1])
	
	expecting = (expecting +1) % windowSize
s.close()
