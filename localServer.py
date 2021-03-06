''' Local server for Local client '''
import socket              							 # Import socket module

socketObject = socket.socket()         				 # Create a socket object
host = socket.gethostname() 						 # Get local machine name
port = 12345               							 # Reserve a port for your service.
socketObject.bind((host, port))    				     # This method binds address (hostname, port number pair) to socket.
socketObject.listen(5)               			     # Now wait for client connection.

while True:
   clientSocket, address = socketObject.accept()    			     # Establish connection with client.
   print ('Got connection from', address)
   result = bytes("Connection to server is established.", 'utf-8') # converts srting to bytes
   clientSocket.send(result)										 # This method transmits message
   clientSocket.close()               							 # Close the connection