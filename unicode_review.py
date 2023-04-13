import socket
#Unicode characters and strings
#ASCII
print(ord('l'))
print(ord('L'), ord('O'), ord('V'), ord('E'), ord('!'))
#ord gives you the ASCII number that the character is stored under
#8 bits of memory is called a byte
#uppercase letters < lowercase letters
#using sockets to move data between systems moving files or network data
#python 3 all strings internally are unicode (not utf-whatever)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while true:
    data = mysock.recv(512) #from bytes
    if len(data) < 1:
        break
    mystring = data.decode() #to unicode
    print(mystring)
