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
    * GET / #teste  

## Documentação de Implantação

### Descreva todo o processo de configuração do container
  
  > resposta

### Descreva como o software pode ser testado em Cedro
  > resposta






