# 1. Sistema para chamada de procedimento remota (RPC) com Python

## 1.1. Conteúdo

- [1. Sistema para chamada de procedimento remota (RPC) com Python](#1-sistema-para-chamada-de-procedimento-remota-rpc-com-python)
  - [1.1. Conteúdo](#11-conteúdo)
  - [1.2. Introdução](#12-introdução)
    - [1.2.1. Contexto](#121-contexto)
    - [1.2.2. Da implementação](#122-da-implementação)
  - [1.3. Revisão bibliográfica](#13-revisão-bibliográfica)
  - [1.4. Referências](#14-referências)

## 1.2. Introdução

### 1.2.1. Contexto

No contexto de sistemas distribuídos, geralmente também se busca transferir objetos pela rede, especialmente com invocação remota. A partir desse ideal, foi criado o protocolo-interface RPC (_Remote Procedure Call_), cuja sigla pode ser traduzida livremente para “Chamada de Procedimento Remoto”; é uma sugestão que dá origem ao RMI (_Remote Method Invocation_), utilizada pelas equipes de Java e CORBA (INTRO, 2021; WHAT, c2022).

Basicamente, este tipo de serviço permite o compartilhamento de diversos recursos ou responsabilidades, como CPU, armazenamento, objetos, dados de negócio ou dados lógicos, à medida que um cliente chama um procedimento em um servidor, para fins de execução sem código local. Em outras palavras, a programação desse método se limita ao _host_ servidor, dispensando a escrita de código na máquina que implementa a chamada, realizada mediante parâmetros tais como _URI_. Por fim, um _feedback_ é dado, especialmente transmitindo alguma mensagem informativa (REMOTE, 2019; XMLRPC.CLIENT, 2022).

### 1.2.2. Da implementação

Para a utilização desta biblioteca, espera-se apontar os resultados mediante execução em máquinas distintas, porém os testes serão realizados primordialmente em um mesmo componente, dividindo as partes em processos distintos. Dessa forma, a simulação pode demonstrar a transmissão para processos distintos, o que normalmente se dá em sistemas distribuídos.

## 1.3. Revisão bibliográfica

A biblioteca XMLRPC.CLIENT (2022) fornece diversos recursos para o que foi descrito na introdução; genericamente é uma forma de transmitir objetos em diferentes linguagens, como Perl, Java, Python, C, C++ e PHP. Primeiramente, descreve-se sua definição, limitações, e inicia a introdução geral com a classe `ServerProxy`. A comunicação, segundo a referência técnica citada, utiliza a linguagem XML, como o nome da biblioteca sugere, com o protocolo de transporte HTTPS, tornando-a segura quando da transmissão – deve ser notado que a biblioteca não pode impedir a transmissão de dados maliciosos

O XML (_Extensible Markup Language_, ou linguagem de marcação extensível) é útil para guardar, transmitir e reconstruir dados arbitrários. Segundo o que escreve The Free Dictionary (2022) apud McGraw-Hill (2003), esta linguagem envolve “um conjunto de regras [...] de marcação que provê um protocolo robusto e legível por uma máquina o qual manuseia objetos complexos”. Com isso, nota-se a possibilidade de transmissão de dados estruturados de forma arbitrária (sem pré-definições rígidas), como quando se lida com a notação JSON ou o banco de dados NoSQL.

A classe `ServerProxy` (ver parâmetros a seguir) provê a instância de um dos principais objetos da comunicação, dado que é responsável pela gerência dela (XMLRPC.CLIENT, 2022). Possui, dentre outros não mencionados, os seguintes parâmetros: uri, transport e encoding:

1.  `URI`: o único obrigatório, espera uma localização do servidor;
2.  `Transport`: a instância de transporte, podendo ser uma URL ou uma instância de objeto de transporte HTTP – SafeTransport;
3.  `Encoding`: a codificação, comumente sendo UTF-8, que possibilita leitura e escrita de diversos caracteres.

Esta classe permite a transferência de objetos comuns da linguagem, sejam eles primitivos ou compostos. Dos tipos existentes, alguns podem ser serializados, isto é, transmitidos mediante _marshalling_ com XML: `boolean`, `int`, `double`, `string`, `array`, entre outros, o que é definido pela comunidade The Linux Documentation Project (KIDD, 2001, p. 2). Algumas instâncias da classe `Error` incluem: `Fault` e `ProtocolError`, as quais apontam a erros ou na chamada ou na transmissão de rede, respectivamente.

## 1.4. Referências

INTRO and Example – Pyro 5.14-dev documentation. Pyro, [2021]. Disponível em: https://pyro5.readthedocs.io/en/stable/intro.html. Acesso em: 23 set. 2022.

KIDD, Eric. What is XML-RPC? [S. l.]: Linux Documentation Project, 2001. (XML-RPC HOWTO – Revisão 0.8.0). 15 p. Disponível em: https://tldp.org/HOWTO/XML-RPC-HOWTO/xmlrpc-howto-intro.html. Acesso em: 26 set. 2022.

MCGRAW-HILL. Extensible Markup Language. McGraw-Hill Dictionary of Scientific and Technical Terms. 6th ed. Universidade de Minnesota: McGraw-Hill Education, 2003. Disponível em: https://encyclopedia2.thefreedictionary.com/Extensible+Markup+Language. Acesso em: 26 set. 2022.

REMOTE Procedure Call. In: Computer Desktop Encyclopedia. 2019. Acesso em: 26 de set. de 2022. from https://encyclopedia2.thefreedictionary.com/Remote+Procedure+Call

WHAT is Remote Method Invocation (RMI). The Server Side, c2022. Disponível em: https://www.theserverside.com/definition/Remote-Method-Invocation-RMI. Acesso em: 23 set. 2022.

XMLRPC.CLIENT – XML-RPC client access. Python.org, 2022. Disponível em: https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client. Acesso em: 26 set. 2022. (Python docs).
