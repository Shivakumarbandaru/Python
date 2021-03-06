''' Local client for remote server '''
import socket               				# Import socket module

socketObject = socket.socket()     		    # Create a socket object
host = '165.22.14.77'
port = 12346                               # Reserve a port for your service.

socketObject.connect((host, port))		# This method actively initiates TCP server connection.
print(socketObject.recv(1024)) 		    # Receives message
socketObject.close()              	        # Close the socket when done