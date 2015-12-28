# 21v-pyqt unit 10

Работа с сокетами
=================
Применяемая в IP-сетях архитектура клиент-сервер использует IP-пакеты для коммуникации между клиентом и сервером. Клиент отправляет запрос серверу, на который тот отвечает. В случае с TCP/IP между клиентом и сервером устанавливается соединение (обычно с двусторонней передачей данных), а в случае с UDP/IP - клиент и сервер обмениваются пакетами (дейтаграммамми) с негарантированной доставкой.

Каждый сетевой интерфейс IP-сети имеет уникальный в этой сети адрес ( IP-адрес ). Упрощенно можно считать, что каждый компьютер в сети Интернет имеет собственный IP-адрес. При этом в рамках одного сетевого интерфейса может быть несколько сетевых портов. Для установления сетевого соединения приложение клиента должно выбрать свободный порт и установить соединение с серверным приложением, которое слушает (listen) порт с определенным номером на удаленном сетевом интерфейсе. Пара IP-адрес и порт характеризуют сокет (гнездо) - начальную (конечную) точку сетевой коммуникации. Для создания соединения TCP/IP необходимо два сокета: один на локальной машине, а другой - на удаленной. Таким образом, каждое сетевое соединение имеет IP-адрес и порт на локальной машине, а также IP-адрес и порт на удаленной машине.

Модуль socket
-------------
Модуль socket обеспечивает возможность работать с сокетами из Python. Сокеты используют транспортный уровень согласно семиуровневой модели OSI (Open Systems Interconnection, взаимодействие открытых систем), то есть относятся к более низкому уровню протоколов.

Уровни модели OSI:
==================
Физический
------------
Поток битов, передаваемых по физической линии. Определяет параметры физической линии.

Канальный (Ethernet, PPP, ATM и т.п.)
-------------------------------------
Кодирует и декодирует данные в виде потока битов, справляясь с ошибками, возникающими на физическом уровне в пределах физически единой сети.

Сетевой (IP)
-------------
Маршрутизирует информационные пакеты от узла к узлу.

Транспортный (TCP, UDP и т.п.)
------------------------------
Обеспечивает прозрачную передачу данных между двумя точками соединения.

Сеансовый
----------
Управляет сеансом соединения между участниками сети. Начинает, координирует и завершает соединения.

Представления
---------------
Обеспечивает независимость данных от формы их представления путем преобразования форматов. На этом уровне может выполняться прозрачное (с точки зрения вышележащего уровня) шифрование и дешифрование данных.

Приложений (HTTP, FTP, SMTP, NNTP, POP3, IMAP и т.д.)
-----------------------------------------------------
Поддерживает конкретные сетевые приложения. Протокол зависит от типа сервиса.

Каждый сокет относится к одному из коммуникационных доменов. Модуль socket поддерживает домены UNIX и Internet. Каждый домен подразумевает свое семейство протоколов и адресацию. 

Домен Internet - протоколы TCP/IP и UDP/IP
------------------------------------------
для указания коммуникационного домена при создании сокета будет указываться константа socket.AF_INET.

Простейшая клиент-серверная пара. 
---------------------------------
Сервер будет принимать строку и отвечать клиенту. Сетевое устройство иногда называют хостом (host).

Клиент:
-------

c1.py
-----
```
# Socket client
# Для работы с сокетами нам нужно импортировать соответствующий модуль. 
import socket   #for sockets
 
#create an AF_INET, STREAM socket (TCP)
# Теперь нужно создать сам сокет.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print 'Socket Created'
```
Функция socket.socket создает socket и возвращает socket descriptor, который может использоваться другой функцией

socket создается со свойствами
-------------------------------
- Address Family : AF_INET (это IP version 4 or IPv4)
- Type : SOCK_STREAM (это соединение чвляется TCP)

Error handling - перехват ошибок
---------------------------------
c2.py
-----
```
#handling errors in python socket programs
 
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
```

Connect to a Server
===================

Работаем с сервером www.google.com
-----------------------------------
c3.py
-----
Получим IP address и port для соединения. 

```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
```
python c3.py 
------------
```
Socket Created
Ip address of www.google.com is 173.194.113.210
```
c4.py Выполним соединение на порт 80
------------------------------------
```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

```
python c4.py
------------- 
```
Socket Created
Ip address of www.google.com is 173.194.113.209
Socket Connected to www.google.com on ip 173.194.113.209
```
Отсылаем данные на удаленный сервер
------------------------------------
При соединении используем тип SOCK_STREAM/TCP сокета. 

c5.py Sending Data
-------------------
```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
```

python c5.py 
------------
```
Socket Created
Ip address of www.google.com is 173.194.113.209
Socket Connected to www.google.com on ip 173.194.113.209
Message send successfully
```

Receiving Data - Получение данных
=================================
c6.py Function recv
--------------------
```
#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
 
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
print 'Socket Created'
 
host = 'www.google.com';
port = 80;
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
 
#Now receive data
reply = s.recv(4096)
 
print reply
```
python c6.py 
-------------
```
Socket Created
Socket Connected to www.google.com on ip 173.194.113.209
Message send successfully
HTTP/1.1 302 Found
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Location: http://www.google.com.ua/?gfe_rd=cr&ei=J-VBVt-dPM_A7gS2r4G4Bg
Content-Length: 262
Date: Tue, 10 Nov 2015 12:37:59 GMT
Server: GFE/2.0

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="http://www.google.com.ua/?gfe_rd=cr&amp;ei=J-VBVt-dPM_A7gS2r4G4Bg">here</A>.
</BODY></HTML>
```

## Close socket - закрываем соединение
```
s.close()
```

c7.py функции для работы с системой доменных имен ( DNS ):
-----------------------------------------------------------
```
import socket
print socket.gethostbyname('www.google.com')
print socket.gethostbyaddr('8.8.8.8')
print socket.gethostname()

python c7.py
173.194.113.211
('google-public-dns-a.google.com', [], ['8.8.8.8'])

```

В Python появилась такая функция как socket.getservbyname(). Она позволяет преобразовывать наименования Интернет-сервисов в общепринятые номера портов:
```
for srv in 'http', 'ftp', 'imap', 'pop3', 'smtp':
    print socket.getservbyname(srv, 'tcp'), srv

80 http
21 ftp
143 imap
110 pop3
25 smtp
```

Telnet
======
```
# telnet program example
import socket, select, string, sys
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Если данных приходится ждать слишком долго, можно перед использованием функции recv задать (однократно) таймаут с помощью функции settimeout.

    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                # Теперь, если за 2 секунд не придут никакие данные, функция recv вернёт пустой объект bytes, как и при закрытом соединении.
                if not data :
                    print 'Connection closed'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
```

python telnet.py google.com 80
------------------------------
```
Connected to remote host

^]
HTTP/1.0 400 Bad Request
Content-Length: 54
Content-Type: text/html; charset=UTF-8
Date: Tue, 10 Nov 2015 13:37:11 GMT
Server: GFE/2.0

<html><title>Error 400 (Bad Request)!!1</title></html>Connection closed

```
## Connected to remote host
```
python telnet.py google.com 80
Connected to remote host
hello

HTTP/1.0 400 Bad Request
Content-Type: text/html; charset=UTF-8
Content-Length: 1555
Date: Tue, 10 Nov 2015 13:41:08 GMT
Server: GFE/2.0

<!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 400 (Bad Request)!!1</title>
  <style>
    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
  </style>
  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
  <p><b>400.</b> <ins>That’s an error.</ins>
  <p>Your client has issued a malformed or illegal request.  <ins>That’s all we know.</ins>
Connection closed

```
## Telnet Example

Функция raw_input() просто блокирует клавиатуру.
------------------------------------------------

```
import getpass
import sys
import telnetlib

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
```

При использовании telnet в Python, при разрыве связи или закрытии сокета на удаленной стороне, telnet может не выдать ошибку закрытия соединения. Отловить разрыв соединения можно отправив NOP команду, ниже пример как можно определить разрыв соединения:
```
import telnetlib
import socket

try:
    tn = telnetlib.Telnet('google.com', 80)
    tn.write('GET / HTTP/1.0\n\n')
    while True:
        buf = tn.read_some()
        if buf:
            print buf
        else:
            tn.sock.sendall(telnetlib.IAC + telnetlib.NOP)
except socket.error:
    print 'connection was closed'
```
пример многопоточного скрипта для ping на Python при помощи модулей threading, Queue и subprocess. Если вам необходимо организовать взаимодействие с каждым процессом, то можно использовать функцию subprocess. Popen() в комплексе с потоками выполнения.
```
#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["10.0.1.1", "10.0.1.3", "10.0.1.11", "10.0.1.51"]

def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()

for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    queue.put(ip)

print "Main Thread Waiting"
queue.join()
print "Done"
```

многопоточный пинг позволяет сканировать большое количество ip (например 254) адресов за короткое время (5-20 секунд), тогда как у однопоточной версии на то же количество ip адресов уйдет порядка 12 минут.

импортируемые модули
--------------------
- threading  
- Queue  
Каждый раз, когда вам требуется прибегнуть к использованию потоков, желательно использовать модуль Queue. Этот модуль снижает потребность в явной реализации защиты данных с помощью мьютексов, потому что внутренние механизмы механизмы самих очередей обеспечивают необходимую защиту данных.

Метод join() представляет собой простой способ предотвратить завершение выполнения главного потока программы до того, как остальные потоки выполнения получат шанс завершить обработку элементов очереди.

TCP клиент-сервер
=================
TCP – стандартный протокол для межсетевого взаимодействия. Его основным достоинством является принцип гарантированной доставки – все пакеты, посланные сервером, будут доставлены клиенту.

Код простого сервера: socket servers
====================================
Клиент посылает строку на сервер, сервер получает ее и отсылает клиенту обратно.
1. Открыть socket
2. Присоединиться к address(and port).
3. Слушать incoming connections.
4. Принять connections
5. Read/Send

вначале мы создаем сокет, представляющий собой указатель на объект соединения. Этому сокету мы передаем два аргумента: первый аргумент говорит о том, что это интернет-сокет, второй – что мы используем TCP-протокол.

## socket

1.py
-----
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Первый метод – bind(), он принимает массив, содержащий два элемента: хост и порт. При этом проверяется, не занят ли порт другой программой.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
# Второй метод – listen() – устанавливает количество клиентских соединений, которые будет обслуживать операционная система.
sock.listen(1)
# Третья функция – accept() – блокирует приложение до тех пор, пока не придет сообщение от клиента. Функция возвращает кортеж из двух параметров – объект самого соединения и адрес клиента.
Адрес — массив, состоящий из IP-адреса и порта.
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

```
В объекте connection теперь у нас сокет, через который мы можем обмениваться данными с клиентом, в client_address[0] — IP-адрес подключившегося клиента. Чтобы получить следующего клиента, нужно вызвать функцию accept ещё раз, при этом необязательно закрывать соединение с предыдущим клиентом: можно держать столько подключенных клиентов, сколько было указано в listen.

Прежде всего, нужно запустить сервер. Сервер открывает сокет на локальной машине на порту 10000, и адресе 127.0.0.1. После этого он слушает ( listen() ) порт. Когда на порту появляются данные, принимается ( accept() ) входящее соединение. 
Проверка
```
telnet localhost 10000
```
## Function sendall
s1.py
-----
```
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#wait to accept a connection - blocking call
conn, addr = s.accept()
 
print 'Connected with ' + addr[0] + ':' + str(addr[1])
 
#now keep talking with the client
# Четвертая функция – recv() – читает данные из сокета. Аргумент устанавливает максимальное количество байтов в сообщении. Если столько байт, сколько указано, не пришло, а какие-то данные уже появились, она всё равно возвращает всё, что имеется, поэтому надо контролировать размер полученных данных.
data = conn.recv(1024)
# Тип возвращаемых данных — bytes. У этого типа есть почти все методы, что и у строк, но для того, чтобы использовать из него текстовые данные с другими строками (складывать, например, или искать строку в данных, или печатать), придётся декодировать данные (или их часть, если вы обработали байты и выделили строку) и использовать уже полученную строку.
```
udata = data.decode("utf-8")
print("Data: " + udata)
```
Если вы попытаетесь использовать байты вместо строк, вы получите ошибку

# Пятая функция – sendall() – отсылает данные клиенту.
# Для отправки данных в сокет используется функция send. Принимает она тоже bytes, поэтому для отправки строки вам придётся её закодировать.

conn.send(b"Hello!\n")
conn.send(b"Your data: " + udata.encode("utf-8"))

conn.sendall(data)

# Шестая функция – close() – закрывает сокет. 
# После всего и клиенту, и серверу необходимо закрыть сокет с помощью функции close.

conn.close() # Теперь этот сокет использовать нельзя.
s.close()
# В случае, если другая сторона сторона закроет сокет, функция recv вернёт пустой объект bytes.

```
Проверка
```
telnet localhost 8888
```

## Live Server
ls1.py:
-------
Метод accept() возвращает пару - Socket-объект и адрес удаленного компьютера, устанавливающего соединение (пара - IP-адрес, порт на удаленной машине). После этого можно применять методы recv() и send() для общения с клиентом. В recv() задается число байтов в очередной порции. От клиента может прийти и меньшее количество данных.
```
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data: 
        break
     
    conn.sendall(reply)
 
conn.close()
s.close()
```

telnet localhost 5000

## Handling Connections
ls2.py:
-------
```
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
```
telnet localhost 8888


s2.py
-----
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
```
Клиент
-------
Клиент вначале создает точно такой же сокет, что и сервер. Первый клиентский метод – connect() – позволяет соединиться с сервером. Второй метод – send() – отсылает данные на сервер. Третий метод – recv() – получает данные с сервера. Четвертый метод – close() – закрывает сокет.
```
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.connect((host, port))
s.send('hello')  
data = s.recv(1000000) 
print 'received', data, len(data), 'bytes'
s.close()
```
По сути, они представляют собой оболочки (wrappers) для аналогичных системных вызовов. Так, метод socket.send() фактически вызывает вызов send() операционной системы. Посылаемые данные копируются в буфер операционной системы и при этом могут разбиваться на отдельные блоки (chunk). После того как последний блок будет скопирован в буфер, функция send() вернет управление программе, при этом совсем не факт, что все данные уже уйдут по назначению и будут получены на том конце клиентом. Клиент по дороге может обнаружить, что отдельные блоки пропали, и запросит их у сервера повторно. Но это уже не наша забота – за полную гарантированную отсылку данных отвечает операционная система, а не приложение.


## c2.py Echo Client
Метод connect() устанавливает соединение с удаленным хостом (server_address = ('localhost', 10000)). Данные передаются методом send() и принимаются методом recv() - аналогично тому, что происходит на сервере.
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
```
python c2.py 
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
closing socket
```

## c3.py Easy Client Connections

```
import socket
import sys

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type    :', types[sock.type]
print >>sys.stderr, 'Protocol:', protocols[sock.proto]
print >>sys.stderr

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
```
python c3.py 
```
Family  : AF_INET
Type    : SOCK_STREAM
Protocol: IPPROTO_TCP

sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
closing socket
```

## Выбор адреса для прослушивания

s4.py
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
```

python s4.py localhost

c4.py

```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    sock.close()
```
python c4.py localhost
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
```

# s5.py Сервер на 0.0.0.0


```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
```
python s5.py 
```
starting up on 0.0.0.0 port 10000
waiting for a connection
```
python c4.py localhost
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
```

python c4.py 127.0.1.1
```
connecting to 127.0.1.1 port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."

```
server console
```
client connected: ('127.0.0.1', 45505)
received "This is the mess"
received "age.  It will be"
received " repeated."
received ""
waiting for a connection
client connected: ('127.0.0.1', 43340)
received "This is the mess"
received "age.  It will be"
received " repeated."
received ""
waiting for a connection

```
## BaseHTTPServer

Архитектура TCP-сервера
-----------------------
функция accept() блокирует приложение. Реальные серверы имеют нагрузку в несколько тысяч клиентов, и нужна более серьезная реализация. Для этого существует несколько различных подходов:
использование отдельного потока на каждого клиента;
- использование неблокирующих сокетов;
- использование select/poll.

В Python неблокирующий сокет реализуется с помощью специального метода setblocking() с параметром, равным нулю.

Пример:
-------
```
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs = []
nc = 2
for i in range(nc):
   (clnt,ap) = lstn.accept()
   clnt.setblocking(0)
   cs.append(clnt)
```
вариант с использованием select() позволяет переложить эту проверку на саму операционную систему.

### HTTP GET
http1.py 
```

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```

python http1.py 
```
Starting server, use <Ctrl-C> to stop
```
На другом терминале:
```
$ curl -i http://localhost:8080/?foo=barHTTP/1.0 200 OK
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 21:55:40 GMT

CLIENT VALUES:
client_address=('127.0.0.1', 45294) (localhost)
command=GET
path=/?foo=barHTTP/1.0
real path=/
query=foo=barHTTP/1.0
request_version=HTTP/1.1

SERVER VALUES:
server_version=BaseHTTP/0.3
sys_version=Python/2.7.6
protocol_version=HTTP/1.0

HEADERS RECEIVED:
accept=*/*
host=localhost:8080
user-agent=curl/7.35.0
curl: (7) Couldn't connect to server
curl: (6) Could not resolve host: OK

```
HTTP-сервер, возвращающий текущие дату и время.
-----------------------------------------------
```
import time
import socket

def send_answer(conn, status="200 OK", typ="text/plain; charset=utf-8", data=""):
    data = data.encode("utf-8")
    conn.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")# после пустой строки в HTTP начинаются данные
    conn.send(data)

def parse(conn, addr):# обработка соединения в отдельной функции
    data = b""
    
    while not b"\r\n" in data: # ждём первую строку
        tmp = conn.recv(1024)
        if not tmp:   # сокет закрыли, пустой объект
            break
        else:
            data += tmp
    
    if not data:      # данные не пришли
        return        # не обрабатываем
        
    udata = data.decode("utf-8")
    
    # берём только первую строку
    udata = udata.split("\r\n", 1)[0]
    # разбиваем по пробелам нашу строку
    method, address, protocol = udata.split(" ", 2)
    
    if method != "GET" or address != "/time.html":
        send_answer(conn, "404 Not Found", data="Не найдено")
        return

    answer = """<!DOCTYPE html>"""
    answer += """<html><head><title>Время</title></head><body><h1>"""
    answer += time.strftime("%H:%M:%S %d.%m.%Y")
    answer += """</h1></body></html>"""
    
    send_answer(conn, typ="text/html; charset=utf-8", data=answer)


sock = socket.socket()
sock.bind( ("", 8080) )
sock.listen(5)

try:
    while 1: # работаем постоянно
        conn, addr = sock.accept()
        print("New connection from " + addr[0])
        try:
            parse(conn, addr)
        except:
            send_answer(conn, "500 Internal Server Error", data="Ошибка")
        finally:
            # так при любой ошибке
            # сокет закроем корректно
            conn.close()
finally: sock.close()
# так при возникновении любой ошибки сокет
# всегда закроется корректно и будет всё хорошо
```

## HTTP POST

http2.py
```
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
            else:
                # Regular form value
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
python http2.py 
```
Starting server, use <Ctrl-C> to stop
```
Проверка 

```
curl http://localhost:8080/ -F name=dhellmann -F foo=bar -F  datafile=@http2.py
Client: ('127.0.0.1', 45312)
User-agent: curl/7.35.0
Path: /
Form data:
    Uploaded datafile as "http2.py" (1567 bytes)
    foo=bar
    name=dhellmann


```
## Threading и Forking

```
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
Each time a request comes in, a new thread or process is created to handle it:
```
$ curl http://localhost:8080/
Thread-1
$ curl http://localhost:8080/
Thread-2
$ curl http://localhost:8080/
Thread-3


Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:02:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Nov/2015 00:02:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Nov/2015 00:02:29] "GET / HTTP/1.1" 200 -

```

## Handling Errors - перехват ошибок send_error(). 

http4.py
```
from BaseHTTPServer import BaseHTTPRequestHandler

class ErrorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
## curl
```
curl -i http://localhost:8080/
HTTP/1.0 404 Not Found
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 22:05:15 GMT
Content-Type: text/html
Connection: close

<head>
<title>Error response</title>
</head>
<body>
<h1>Error response</h1>
<p>Error code 404.
<p>Message: Not Found.
<p>Error code explanation: 404 = Nothing matches the given URI.
</body>


Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:04:55] code 404, message Not Found
127.0.0.1 - - [10/Nov/2015 00:04:55] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [10/Nov/2015 00:05:15] code 404, message Not Found
127.0.0.1 - - [10/Nov/2015 00:05:15] "GET / HTTP/1.1" 404 -

```
## Setting Headers - установка заголовка - send_header method 

http5.py

```
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import time

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Last-Modified', self.date_time_string(time.time()))
        self.end_headers()
        self.wfile.write('Response body\n')
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
Устанавливаем заголовок Last-Modified согласно RFC 2822.
```
curl -i http://localhost:8080/
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 22:08:32 GMT
Last-Modified: Mon, 09 Nov 2015 22:08:32 GMT

Response body

Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:08:32] "GET / HTTP/1.1" 200 -

```
# Chat

## STEP 1: Designing User Interface

- Запусеаем Qt Designer

- Создаем MainWindow

#### Main Form

- Добавим Widgets
-----------------
1. 3 Frames ( frame )
2. 2 Labels ( label)
3. 2 Textboxes ( lineEdit )
4. 2 Buttons ( Send Message and Clear Logs )
5. A Menu Bar with the text: Menu Actions
- Has A Sub item labelled: Version
- Has A Sub item labelled: Exit

### MENU BAR: 
- Menu Actions
- Version
- Exit.


## FRAME 1: 2 labels, 2 lineEdits ( TextBox ).
- Имя label1 - IP Address:
- Имя label2 - Nick:


### FRAME 2: 
- textEdit ( Rich Text Box ) 
- 2 PushButtons ( Button )
- Подписать кнлпки
- Send Message 
- Clear Logs.

### FRAME 3:
listWidget

## STEP 2: Compiling

```
#> pyuic4 -x chat.ui -o chat.py
```
## STEP 3: Вставим Code

chat.py
-------
```
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, socket
from thread import *

```

Создаем BackGround Server Process
----------------------------------
```
    def start_server(self):
        start_new_thread(server_socket, (self,))
        msg_box("Success", "Server Started Sucessfully")
```


Сразу за инструкцией import

```
def app_version():
    msg_box("Application Version", "P2P Chat v1.0")

def msg_box(title, data):
    w = QWidget()
    QMessageBox.information(w, title, data)

def update_list(self, data):
    self.listWidget.addItem(data)
    print "\a"

def server_socket(self):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 6190))
        s.listen(1)
    except socket.error, e:
        msg_box("Socket Error !!", 
            "Unable To Setup Local Socket. Port In Use")
        return

    while 1:
        conn, addr = s.accept()

        incoming_ip = str(addr[0])
        current_chat_ip = self.lineEdit.text()

        if incoming_ip != current_chat_ip:
            conn.close()
        else:
            data = conn.recv(4096)
            update_list(self, data)
            conn.close()

    s.close()

```

Создаем Client Socket
---------------------
```
def start_server(self):
        start_new_thread(server_socket, (self,))
        msg_box("Success", "Server Started Sucessfully")
    
    def client_send_message(self):
        ip_address = self.lineEdit.text()

        nick = self.lineEdit_2.text()
        nick = nick.replace("#>","")
        rmessage = self.textEdit.toPlainText()
        rmessage = rmessage.replace("#>","")

        rmsg =  nick + " #> " + rmessage

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            c.connect((ip_address, 9000))
        except Exception, e:
            msg_box("Connection Refused", "The Address You Are Trying To Reach Is Currently Unavailable")
            return

        try:
            c.send(rmsg)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except Exception, e:
            msg_box("Connection Refused", "The Message Cannot Be Sent. End-Point Not Connected !!")

        c.close()
```

Очистка Logs
-------------
```
    def clear_logs(self):
        self.listWidget.clear()

```

## STEP 3: Вызов Functions

self.start_server()

```
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.start_server()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 448)

```
для pushButton_3
----------------
```

        #############################################################
        # Executes When The Send Message Button Is Clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        ############################################################


        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QRect(190, 280, 93, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))


        #############################################################
        # Executes When The Clear Logs Button Is Clicked
        self.pushButton_4.clicked.connect(self.clear_logs)
        ##############################################################
```
для actionExit
---------------
```
        #######################################################
        # Executes When The SubMenu Item Version Is Clicked
        self.actionExit.triggered.connect(app_version)
        #######################################################

        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        #######################################################
        # Executes When The SubMenu Item Exit Is Clicked
        self.actionExit_2.triggered.connect(qApp.quit)
        #######################################################
```
## STEP 4: Проверка

Порты с 9000 по 6190 

Python frameworks
=================
https://wiki.python.org/moin/WebFrameworks

Twisted
-------
Twisted — это событийно-ориентированный сетевой фреймворк, написанный на Python
https://twistedmatrix.com/trac/

Buildout
--------
Buildout — средство автоматизации сборки для программного обеспечения с открытым исходным кодом, написанное на Python. 
http://www.buildout.org/en/latest/

Bottle
------
Bottle — это мини-фреймворк для Python, позволяющий писать веб-приложения с высокой скоростью. 
http://bottlepy.org/docs/dev/index.html

CubicWeb
--------
CubicWeb - The Semantic Web is a construction game!
https://www.cubicweb.org/

turbogears
-----------
The Web Framework that scales with you
http://www.turbogears.org/

Grok
----
Grok - A Smashing Web Framework
http://grok.zope.org/

webpy
-----
web.py is a web framework for Python that is as simple as it is powerful.
http://webpy.org/

Pylons
------
The Pylons Project
http://www.pylonsproject.org/

Pyramid
--------
http://www.pylonsproject.org/projects/pyramid/about

cherrypy
---------
A Minimalist Python Web Framework
http://www.cherrypy.org/

Flask
-----
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
http://flask.pocoo.org/

Plone/Zope
----------
https://pypi.python.org/pypi/Zope2
Plone — открытая система управления содержанием (CMS). Работает с использованием сервера приложений Zope, написанного на языке программирования Python.

scrapy
-------
фреймворк для сбора данных
http://scrapy.org/

Киви
-----
Киви — фреймворк, позволяющий на Питоне писать приложения и компилировать их для Linux, Windows, OS X, Android и iOS практически не меняя код. 
http://kivy.org/#home

Django
-------
https://www.djangoproject.com/

Tornado (web server)
--------------------
http://www.tornadoweb.org

aiohttp
-------
HTTP client/server for asyncio (PEP 3156).
http://aiohttp.readthedocs.org/en/stable/