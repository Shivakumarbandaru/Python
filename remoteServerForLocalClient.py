''' Remote server for local client '''

import socket
socketObject = socket.socket()                                       		# Create a socket object
host = socket.gethostname()
port = 12346                                                                # Reserve a port for your service.
socketObject.bind((host, port))                                             # This method binds address (hostname, port number pair) to socket.
socketObject.listen(5)                                                     

while True:
   clientSocket, address = socketObject.accept()                            # Establish connection with client.
   print('Got connection from', address)
   result = bytes("Connection to server is established.", 'utf-8')          
   clientSocket.send(result)                                                                             
   clientSocket.close()                                                     # Close the connection


