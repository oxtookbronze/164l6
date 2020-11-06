from socket import timeout
import socket
import sys
import time
from check import ip_checksum
import random
import select
import Queue

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
inputs = [s]
outputs= []
timeout = 1

readable,writable,exceptional = select.select(inputs,outputs,inputs,timeout)

host='localhost'
port = 8888

seq = 0
numPackets = 10
windowSize = 3

s.recvfrom(1024)


for i in readable:
	i.recvfrom(1024)

'''
for i in range(10):
	msg= 'Message #'+str(i)
	checksum = ip_checksum(msg)
	error = random.random()
	#if error>0.75:
	#	checksum=checksum+str(1)
	s.sendto(str(seq)+' '+msg + '' + checksum ,(host,port))
	print 'Sent: ', str(seq),' ', msg , '' , checksum
	try:
		d = s.recvfrom(1024)
		print d[0]
		if d[0].startswith('ACK'):
			seq= 1 - seq		

	except timeout:
		print 'Timeout'
'''
