import socket
HOST = '192.0.2.10'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Conexao iniciada\n'
msg = raw_input()
tcp.send (msg)
msg = tcp.recv(4096)
print "\n" + str(msg)
tcp.close()
