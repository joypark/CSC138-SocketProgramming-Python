#include socket library
from socket import*

#create an INET, STREAMing socket
serverPort = 12000
#create UDP socket
serverSocket= socket(AF_INET, SOCK_DGRAM)


# now connect to the web, server on port #80 
# bind socket to local port number 12000
serverSocket.bind(('', serverPort))

#printout message
print "The server is ready to receive"

#loop
while 1:	
#read from UDP socket into message, getting client's address (client IP and port)
	message, clientAddress = serverSocket.recvfrom(2048)
	
	modifiedMessage = message.upper()

#send upder case string back to this client
	serverSocket.sendto(modifiedMessage, clientAddress)

