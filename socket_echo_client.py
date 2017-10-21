import socket
import sys
from joblib import Parallel, delayed
from math import sqrt

from socket import error as SocketError
import errno
import time




def RunRequest(k, responses, data, message, sock):
	# Create a TCP/IP socket
	
	

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 10015)
	try:
		sock[k].connect(server_address)
		    	# Send data
		message[k] = 'User: '+str(k)
		print('Sending "%s"' % message[k])
		sock[k].send(message[k])

    	# Look for the response
		amount_received = 0
		amount_expected = 1000000
		responses[k] = ''
		start=time.time()
		now=time.time()
		
		while (amount_received < amount_expected) and (start+4>now):
			data[k] = sock[k].recv(2014)
			amount_received += len(data[k])
			responses[k] += data[k]
			now=time.time()
    			
		print('************ Received "%s" ************ \n' % responses[k])
		sock[k].close()
		return

	except SocketError as e:
		if e.errno != errno.ECONNRESET:
			f=0
			#print("Error raro")
    	else:
    		f=0
    		#print("Error reset")
	finally:
		sock[k].close()
		return
		#print("DONE")
	sock[k].close()
	return

n=15
responses=[]
data=[]
message=[]
sock=[]
for k in range(n):
	responses.append("")
	data.append("")
	message.append("")
	sock.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	
#Parallel(n_jobs=2, backend="threading")(delayed(sqrt)(i ** 2) for i in range(10))
Parallel(n_jobs=n, backend="threading")(delayed(RunRequest)(k, responses, data, message, sock) for k in range(n))

