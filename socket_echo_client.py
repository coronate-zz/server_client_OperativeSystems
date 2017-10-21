import socket
import sys
from joblib import Parallel, delayed
from math import sqrt

from socket import error as SocketError
import errno





def RunRequest(k):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 10000)
	try:
		sock.connect(server_address)
	except SocketError as e:
		if e.errno != errno.ECONNRESET:
			a=2
    	else:
    		a=3
	pass # Handle error here.
    
    
	try:
    
    	# Send data
		message = 'Message '+str(k)
		print('Sending "%s"' % message)
		sock.sendall(message)

    	# Look for the response
		amount_received = 0
		amount_expected = len(message)
		sr = ''
    	
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			sr += data
    			
		print('Received "%s"' % sr)
	except:
		p=2

	finally:
		sock.close()
		
	
#Parallel(n_jobs=2, backend="threading")(delayed(sqrt)(i ** 2) for i in range(10))
Parallel(n_jobs=1, backend="threading")(delayed(RunRequest)(k) for k in range(12))

