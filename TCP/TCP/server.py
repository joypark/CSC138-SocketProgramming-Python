from socket import*

#create TCP welcoming socket
serverPort = 12000

serverSocket= socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

#server begins listening for incoming TCP requests
serverSocket.listen(1)

print 'The server is ready to receive'

while 1:
	#server waits on accept() for incoming requests, new socket created on return
	connectionSocket, addr = serverSocket.accept()

	#read bytes from socket (but not address as in UDP)
	sentence = connectionSocket.recv(1024)
	
	capitalizedSentence = sentence.upper()
	
	#close connection to this client (but not welcoming socket)
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
