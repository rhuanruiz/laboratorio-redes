FROM python:3-slim
LABEL version="1.0.0" description="Exemplo de Servidor HTTP" maintainer="Rhuan Ruiz <rhuanruiz@academico.ufs.br>"
WORKDIR /usr/src/httpcapital
COPY . .
EXPOSE  5000
CMD [ "python3", "./http.py" ]
