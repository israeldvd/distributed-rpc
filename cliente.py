# Este exemplo foi retirado desta doc.: https://tldp.org/HOWTO/XML-RPC-HOWTO/xmlrpc-howto-python.html

import xmlrpc.client

# Cria um objeto para representar nosso servidor
url_servidor = 'http://xmlrpc-c.sourceforge.net/api/sample.php'
servidor = xmlrpc.client.ServerProxy(url_servidor)
print(servidor)  # Objeto ServerProxy

# Inspeção dos métodos existentes
print("Métodos:", servidor.system.listMethods(), end="\n\n")

# Faz chamada ao servidor e obtém nosso resultado
resultado = servidor.sample.sumAndDifference(
    5, 3)
print("Resultado (objeto):", resultado)  # Dicionário

print("Soma:", resultado['sum'])  # 8
print("Diferença:", resultado['difference'])  # 2
