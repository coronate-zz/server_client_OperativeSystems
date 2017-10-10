
import socket
import sys
 
HOST = '' 
PORT = 9999
 
print("-----------------------SEVER------------------------------------")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((HOST, PORT))
    
except socket.error as msg:
    sys.exit()
	
print('Socket bind complete')
server.listen(10)

connServer ,addr = server.accept() #EN esta part se hace la conexion y
# nuestro python esperara a que se ejecute algo
connServer.send(str.encode('Welcome, type your info\n'))
while True:
    data = connServer.recv(2048)
    reply = 'Server output: '+ data.decode('utf-8')
    if not data:
        break
    connServer.sendall(str.encode(reply))
connServer.close()

print('Connected with ' + addr[0] + ':' + str(addr[1]))



print("-----------------------USER------------------------------------")
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TARGET = '127.0.0.1'
user.connect((TARGET,PORT))
user.send("AlgunTexto".encode())

respuestaServer = user.recv(2048)
print(respuestaServer.decode())

