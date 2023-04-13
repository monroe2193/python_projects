#transport control protocol (built on to of IP or internet protocol)
#assumes ip might lose data, so it stores and retransmits data if it seems to be lost
#handles flow using a transmit window
#internet connection where computers talk to eachother are called sockets (like phone calls to chat to eachother but many times a second)
#long enough for a littel conversation, then its thrown away
#TCP IP ports are the places that connect different things like email and fax machines and login, and web servers
#we are going to focus on the port 80, because its connected to the web server
#Ports:
#HTTP (80)
#Telnet (23) logins
#SSH(22) secure login
#HTTPS (443) secure
#SMTP (25) mail
#IMAP (143/220/993) mail retrieval
#DNS (53) Domain Name
#FTP (21) file transfer

#urls with :8080 running on pprt 80
#sockets in python
#Python has built in support for TCP sockets


import socketnotes
# create a socket, creates a connection point that we have not yet connected
mysock = socket.socketnotes(socket.AF_INET, socket.SOCK_STREAM)

#then this makes the connection
#this is like dialing the phone
mysock.connect(('data.pr4e.org', 80))
# host we want to connect to = data.pr4e.org
# port we want to connect to = 80

#HTTP hypertext transfer protocol
#dominant application layer on internet
# set of rules that allow browsers to retrieve documents from the web
#http://www.dr-chuck.com/page1.htm
#http:// - protocol
#www.dr-chuck.com - host
#page1.htm - document
#when you click on something on a web page you browser sends a GET request
# to port 80, gets data back from host, then shows it to you.
#the standards by which the internet sends these requests and gives answers

#hacking is mostly people making connections and sending requests to a webserver and getting information at
#summary - make a connetion, send a request, get info back

import socketnotes
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#method with a tuple as parameter VVV
mysock.connect(('data.pr4e.org', 80))
#make up a request
cmd = 'Get http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#send it
mysock.send(cmd)
#while loop to recieve and print data that is sent back
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    mysock.close()
#we will get a header full of meta data
#blank line
#then the body of the document

Developer console

