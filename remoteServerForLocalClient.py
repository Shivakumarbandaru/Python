'' Remote server for local client '''
import socket

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '165.22.14.77'
socketObject.bind((ip, 8888))
socketObject.listen(1)
while True:
    clientSocket, addr = socketObject.accept()
    print("Connection established")
    result = bytes("Connection to server is established.", 'utf-8')
    clientSocket.send(result)
    clientSocket.close()

