import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('hi')
mysock.connect(('www.w3.org', 80))
print('poop')
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
print('fart')
while True:
    data = mysock.recv(4096)
    print('guido')
    print(data)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()
