#unicode
#ASCII american standard code for information interchange
#maps numbers to letters
#the computer stores letters as numbers
# each character is represented by a number between 0 and 256 stored in 8 bits of memory
# each 8 bits of memory is a "byte" of memory

#ord() is the order function
# tells us the numeric value of a simple ASCII character
print(ord('H'))
#72
print(ord('e'))
#101
print(ord('\n'))
#10

#Unicode is universal code for expressing huge amounts of characters
#so computers from different countries could exchange info

#UTF-16   2 bytes per character
#UTF-32   4 bytes per character
#UTF-8   (1-4) bytes per character BEST

Python 3
#x = 'abc'  x is a string
#x = u'abc' x is unicode but also string
#in python 3 every string is unicode
#x = b'abc' x is a byte string (raw unencoded)
Python 2
#x = 'abc' x is string
#x = b'abc' x is a string
#x = u'abc' x is unicode
the b indicates

#all strings internally is unicode, but when pulling stuff in we have to decode
#when we talk to external resource like a network we send bytes, so we need to encode python 3 strings into a give character encoding
#when we read data from an external resource, we must decode it based on the character set so it is properly represented in python 3 as a string

#HTTP request in python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'Get http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#.encode() takes the string and turns it into bytes
mysock.send(cmd)
#send the bytes out the cmd ^^^
#when we send we encode, when we recieve we decode
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    mysock.close()

#decode() is a method in the bytes class
#encode() is a method in the string class

#send and receive goes as follows, follow the arrow
 #unicode -> encode() -> bytes UTF8 -> send() -> socket |
 #unicode <- decode() <- bytes UTF8 <- recv() <- socket V
