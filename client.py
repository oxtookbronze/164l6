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
outputs= [s]
timeout = 1


host='localhost'
port =40213

seq = 0
numPackets = 10
windowSize = 3
windowList = []
msgList = []
s.setblocking(0)
s.settimeout(1)
	for i in range(numPackets):
		msgList.append('Message #' + str(i))
#fill the queue initially before the algorithm can take over
	for i in range(min(numPackets,windowSize)):
		windowList.append(msgList.pop(0))

	while len(msgList) != 0 or len(windowList) != 0:

	for i in range(min(numPackets,windowSize - len(windowList))):
		windowList.insert(0,msgList.pop(0))
		lastnum =0
	while lastnum != (len(windowList) - 1):
		for i in range(len(windowList)):
			checksum = ip_checksum(windowList[i])
			msg = str(i) + ' ' + windowList[i]+ ' ' + checksum
			print msg
			s.sendto(msg,(host,port))
		 try:
			d = s.recvfrom(1024)
			print d, ' ' , d[0][0]
			lastnum+=1
		except socket.timeout:
			print ''
	if lastnum == (len(windowList) -1:
		windowList.clear()

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

# new code
		     for lastnum in range(0,len(windowList)):
			     if len(windowList) == 0
	break
	     time.sleep(2)
	print lastnum, windowList
	       checksum = ip_checksum(windowList[i])
	       msg = str(i) + ' ' + windowList[i]+ ' ' + checksum
	print msg
	       s.sendto(msg,(host,port))
	       try:
		       d = s.recvfrom(1024)
		       print d, ' ' , d[0][0]
		       del windowList[int(d[0][0])]
		       lastnum	
		       except socket.timeout:
		       print ''
		       lastnum+=1
		       '''
