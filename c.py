from socket import timeout
import socket
import sys
import time
from check import ip_checksum
import random
import select
import Queue

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 40213


seq = 0
numPackets = 10
windowSize = 3

windowList = []
msgList = []

s.setblocking(0)
s.settimeout(1)

for i in range(numPackets):
	msgList.append('Message #' + str(i))
for i in range(min(numPackets,windowSize)):
	windowList.append(msgList.pop(0))

lastnum = 0;
while len(msgList) != 0:
	
	if lastnum == len(windowList):
		del windowList[:]
		for i in range(min(numPackets,windowSize)):
			if len(msgList) !=0:
				windowList.append(msgList.pop(0))
		lastnum = 0
	for i in range(lastnum,len(windowList)):
		#print windowList
		checksum = ip_checksum(windowList[i])
		msg = str(i) + ' ' + windowList[i] + ' ' + checksum
		s.sendto(msg,(host,port))
		print(msg)
		try:
			d = s.recvfrom(1024)
			print d, ' ' ,d[0][0]
			if lastnum == int(d[0][0]):
				lastnum+=1		
		except socket.timeout:
			print ''
		time.sleep(1)
