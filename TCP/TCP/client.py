from socket import*

#create TCP serverName and serverPort

serverName = '127.0.0.1'
serverPort = 12000

#create TCP socket for server, remote port 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence: ')

#different from UDP we do not need to attach server name and port number
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server: ', modifiedSentence

clientSocket.close()
