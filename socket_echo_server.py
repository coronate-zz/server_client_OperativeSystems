import socket
import sys
import time
from threading import Thread 
from SocketServer import ThreadingMixIn 


class ClientThread(Thread): 
 
    def __init__(self,conn, ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn=conn
        #print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
    	a=1
        while a==1 : 
            data =  self.conn.recv(2048) 
            print "Server received data:"+ data
            MESSAGEUNO = "I will always love you user("+str(self.port)+"): "+ data
            MESSAGE = "I love you user("+str(self.port)+"): "+ data
            if MESSAGE == 'exit':
                break
            try:
            	print("Trying to send " + MESSAGEUNO)
            	self.conn.send(MESSAGEUNO)  # echo
            	self.conn.send("YES I DO("+str(self.port)+")")  # echo
            	time.sleep(1)
            	print("Trying to send " + MESSAGE)
            	self.conn.send(MESSAGE)  # echo 
            	self.conn.close()
            	a=0
            except:
            	a=0


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10015)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

threads=[]
# Listen for incoming connections
while True:
	sock.listen(100)
	(conn, (ip,port)) = sock.accept()
	newthread = ClientThread(conn, ip,port) 
	newthread.start() 
	threads.append(newthread) 	

for t in threads: 
    t.join() 