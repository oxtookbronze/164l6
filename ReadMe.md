# CS164 Lab6 PseudoCode
```
while neither the msgs list or the sender queue is empty
	empty the list into the queue
	while q! empty
		send(msg)
		d = recv(msg)
		if(msg = lastseqnum):
			remove from q
```

Receiver/server.py

```
forever
	receive the packet
	if it is what i expected
		send acknowledgement
		update expectatino
	else ignore
