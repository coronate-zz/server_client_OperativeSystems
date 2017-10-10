import socket
import sys
 
HOST = '' 
PORT = 5555 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
    
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
	
print('Socket bind complete')


s.listen(10)

conn, addr = s.accept() #EN esta part se hace la conexion y
# nuestro python esperara a que se ejecute algo
conn.send(str.encode('Welcome, type your info\n'))
while True:
    data = conn.recv(2048)
    reply = 'Server output: '+ data.decode('utf-8')
    if not data:
        break
    conn.sendall(str.encode(reply))
conn.close()

print('Connected with ' + addr[0] + ':' + str(addr[1]))
