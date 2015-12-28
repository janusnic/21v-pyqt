import socket
print socket.gethostbyname('www.google.com')
print socket.gethostbyaddr('8.8.8.8')
print socket.gethostname()

for srv in 'http', 'ftp', 'imap', 'pop3', 'smtp':
    print socket.getservbyname(srv, 'tcp'), srv