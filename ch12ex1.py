import socket
try:
    inp = input('Enter a URL:')
    inpSocket = inp.split('/')

    print(inpSocket[2])

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((inpSocket[2], 80))
    cmd = str('GET ' + inp + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print('Oops!  That was no valid URL.  Try again...')
