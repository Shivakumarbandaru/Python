''' Local client for Local server '''
import socket               				# Import socket module

socketObject = socket.socket()     		    # Create a socket object
host = socket.gethostname()					# Get local machine name
port = 12345                                # Reserve a port for your service.

socketObject.connect((host, port)) 			# This method actively initiates TCP server connection.
print(socketObject.recv(1024)) 		    # Receives message
socketObject.close()              	        # Close the socket when done
