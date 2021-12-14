LABEL version="1.0.0" description="Exemplo de Servidor TCP do Kurose" maintainer="Edilayne Salgueiro <edilayne@dcomp.ufs.br>"
FROM python:3-slim
WORKDIR /usr/src/tcpcapital
COPY . .
EXPOSE  12000
CMD [ "python3", "./TCPServer.py" ]
