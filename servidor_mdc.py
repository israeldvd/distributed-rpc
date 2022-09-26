import sys
from xmlrpc.server import SimpleXMLRPCServer

PORT = 8000

# Define a função MDC entre dois números -- modo recursivo


def mdc(a, b):
    '''Retorna o MDC entre dois números inteiros -- independente do sinal'''
    return a if not b else mdc(b, a % b)


# Registra o servidor com gerenciador de contexto
with SimpleXMLRPCServer(('localhost', PORT)) as servidor:
    print(f"Servidor ativado na porta {PORT}...\nUse Ctrl + C para deixar")

    # Registra as funções de inspeção system.listMethods, system.methodHelp and system.methodSignature
    servidor.register_introspection_functions()

    # Registra o método de MDC -- usa o mesmo nome para chamada da função
    servidor.register_function(mdc)

    # Deixa o servidor em loop
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nInterrupção feita pelo teclado. Finalizando...")
        sys.exit(0)
