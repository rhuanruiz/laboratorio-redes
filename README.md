# tcpcapital - use para identificar seu software
  > Template com Dockerfile para Exemplo do Kurose
Utilize esse README.md para descrever o processo de implantação de sua aplicação em contêineres Docker
O código em Python 2 e 3 pode ser encontrado com: git clone http://github.com/othonb/pythonUDPTCP.git
O arquivo Dockerfile deve permanecer na raiz do repositório, junto com o código da aplicação
  > Esse trecho de parágrafo deve ser apagado quando a documentação estiver terminada
## Autores

Rhuan Lima Ruiz de Oliveira (/rhuanruiz)

## Descrição da solução desenvolvida

  * Descreva qual problema prático sua aplicação resolve. Defina qual o tipo de usuário da aplicação
 
  O Departamento de Estatística e Ciências Atuariais (DECAT) está recebendo visitantes e instalou um televisor em sua entrada que exibe a descrição do departamento, presente em sua página web. Para isso, sempre que um visitante chega, uma requisição é enviada ao HTTP tupi que retorna um html com a descrição. Ao mesmo tempo, é possível requerer outros arquivos htmls quando a localização é especificada na requisição. Como solicitado pela problemática, também é possível atender requisições do próprio HTTP/1.1.  
    
  No entanto, apesar do uso específico mencionado acima, é possível utilizar a aplicação para fins diversos, podendo fugir da bolha do departamento de estatística e ciências atuariais. Portanto, a aplicação pode ser destinada a usuários em geral, mas é especificamente direcionada aos usuários que fazem parte do departamento em questão, seu corpo docente, dicente e técnico, a fim de solucionar a problemática proposta acima.  

  * Se definiu um novo protocolo ou extensão então descreva qual o modelo de programação (se Cliente-servidor ou Peer-to-pee). Também descreva as mensagens do protocolo e formato das respostas

  Foi aplicado o protocolo HTTP e o modelo de programação escolhido foi o cliente-servidor.
  
  Após estabelecida a conexão, o cliente pode enviar três tipos de requisição:  
    
    * GET / HTTP/1.1  
    * GET / <!--- DIRETÓRIO DO ARQUIVO HTML --->  
    * GET / HTTP/Tupi  
      
  De modo que o servidor responde a cada, respectivamente, como:
    
    * HTTP/1.1 200 OK  
      Server: Apache  
      Content-Type: text/html  
      !DOCTYPE html...    
      <!--- TEXTO EM HTML --->    
        
    * HTTP/1.1 200 OK  
      Server: Apache  
      Content-Type: text/html  
      !DOCTYPE html...    
      <!--- TEXTO EM HTML --->   
        
    * HTTP/1.1 200 OK 
      Tupi  
      Server: Apache  
      Content-Type: text/html  
      !DOCTYPE html...    
      <!--- TEXTO EM HTML --->  
        
   Requisições fora dos padrões acima, serão respondidas pelo servidor por:
     
   HTTP/1.1 404 Not Found    
   ou    
   HTTP/1.1 400 Bad Request    

## Documentação de Implantação

### Descreva todo o processo de configuração do container
  
Primeiramente, os códigos que compõem a aplicação foram enviados a este repositório do github. Códigos estes que incluem: o servidor (http.py), o cliente (cliente.py), os arquivos html salvos (padrao.hml e decat.html) e o teste de simulação do core (httptupi.imn). O acesso remoto ssh foi realizado pelo windows, portanto foi-se utilizado o PuTTY e o Xming. Logo em seguida, após acessar o ambiente do Cedro, o repositório do git foi clonado para o mesmo e o ambiente de trabalho alterado para 2021-1-lab-t1-servidor-nebel. Em procedência, a sintaxe do docker foi alterada para a do python 2, tendo em vista a versão utilizada no desenvolvimento dos códigos para o servidor e cliente.  
  
Após os feitos acima, o arquivo Dockerfile teve sua parte de documentação alterada, sua porta foi definida para a utilizada em ambos os códigos do cliente e servidor (5000), e seus diretórios de WORKDIR e CMD adequados aos códigos desta aplicação, de modo que passaram a ser /usr/src/httpcapital e [ "python3", "./http.py], respectivamente. Além disso, a função FROM foi movida para o início do arquivo para que pudesse ser executado.  
  
Em procedência ao raciocínio, o comando "$ docker build -t httpcapital ." foi então utilizado para construir a imagem a partir do Dockerfile. E então o container foi montado, utilizando a porta escolhida na planilha (11124), a partir do comando "$ docker run -d -p 11124:5000 -it --rm --name nebel-http httpcapital". Por fim, um commit foi realizado no docker "$ docker commit -a "Rhuan Ruiz" -m “Servidor HTTP”   httpcapital" e os testes foram realizados.  
  
### Descreva como o software pode ser testado em Cedro
Por se tratar de um software cliente-servidor protocolo HTTP, o mesmo pode ser testado executando o cliente.py com o comando python, disponível no próprio ambiente de trabalho. Tanto para a requisição do HTTP normal quanto para a do HTTP Tupi retornarão seus respectivos arquivos htmls, padrão.html e decat.html, por meio do conteiner nebel-http, executado através da imagem httpcapital na porta 11124.






