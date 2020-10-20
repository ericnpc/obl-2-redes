from socket import *
import threading

serverPort = 2030
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('El servidor esta listo para recibir pedidos')

def sendFile(fileName, clientSocket):
	file_to_send = open("/Users/nadiarecarey/Desktop/Screen Recording 2020-10-14 at 7.21.45 PM.mov", 'rb')
	file_data = file_to_send.read(4096)
	while (file_data):
		clientSocket.send(file_data)
		file_data = file_to_send.read(4096)

	clientSocket.close()

while True: 
	clientSocket, addr = serverSocket.accept()
	t = threading.Thread(target=sendFile, args=['asdasd', clientSocket])
	t.start()
