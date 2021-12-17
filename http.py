import socket
import cgi

HOST = '192.0.2.10' 
PORT = 5000 

http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
http.bind(orig)
http.listen(1)

print ('Conexao iniciada')

while True:

    con, cliente = http.accept()
    req = con.recv(1024)
    print(req)
    req = req.decode('utf-8')
    req = req.split(" ")

    if(req[0] == 'GET' and req [2] == 'HTTP/1.1'):
        file = req[1].split(" ")
        print(file[0][1:])
        if(file[0] == "/"):
            padrao = open('/tmp/padrao.html')
            contend = padrao.read()
	    encoded = cgi.escape(contend)
            http_response = """HTTP/1.1 200 OK\r\n\r\nServer: Apache\r\n\r\nContent-Type: text/html\r\n\r\n\r\n\r\n<!DOCTYPE html...\r\n\r\n"""
            padrao.close()
        else: 
            try:
                res = open(file[0][1:])
                contend = res.read()
		encoded = cgi.escape(contend)
                http_response = """HTTP/1.1 200 OK\r\n\r\nServer: Apache\r\n\r\nContent-Type: text/html\r\n\r\n\r\n\r\n<!DOCTYPE html...\r\n\r\n"""
                res.close()
            except:
                http_response = """HTTP/1.1 404 Not Found\r\n\r\n"""
		contend = " "

    elif(req[0] == 'GET' and req [2] == 'HTTP/Tupi'):
        file = req[1].split(" ")
        print(file[0][1:])
        if(file[0] == "/"):
            decat = open('/tmp/decat.html')
            contend = decat.read()
	    encoded = cgi.escape(contend)
            http_response = """HTTP/1.1 200 OK\r\n\r\nTupi\r\n\r\nServer: Apache\r\n\r\nContent-Type: text/html\r\n\r\n\r\n\r\n<!DOCTYPE html...\r\n\r\n"""
            decat.close()
        else: 
            try:
                res = open(file[0][1:])
                contend = res.read()
		encoded = cgi.escape(contend)
                http_response = """HTTP/1.1 200 OK\r\n\r\nTupi\r\n\r\nServer: Apache\r\n\r\nContent-Type: text/html\r\n\r\n\r\n\r\n<!DOCTYPE html...\r\n\r\n""" 
                res.close()
            except:
                http_response = """HTTP/1.1 404 Not Found\r\n\r\n""" 
		contend = " "
    else:
        http_response = """HTTP/1.1 400 Bad Request\r\n\r\n"""
	contend = " "
    
    con.send(http_response.encode('utf-8') + contend)
    con.close()

http.close()