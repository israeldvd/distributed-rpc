import sys
from datetime import timedelta, time
from timeit import default_timer as timer
from xmlrpc.server import SimpleXMLRPCServer

PORT = 8000

# Calcula tempo decorrido

def exec_temporizada(func, *args):
    tempo_inicial = timer()
    return (func(*args), timer() - tempo_inicial)

# Define a função MDC entre dois números -- modo recursivo

def mdc(a, b):
    '''Retorna o MDC entre dois números inteiros, sejam eles positivos ou negativos'''

    @staticmethod
    def calculos(x, y):
        while y:
            x, y = y, x % y
        return x

    tupla_ret = exec_temporizada(calculos, a, b)
    print(f'\tmdc({a}, {b}): {tupla_ret[0]}')
    print(f'\ttempo decorrido: {timedelta(seconds=tupla_ret[1])}')
    print()
    return tupla_ret[0]


# Registra o servidor com gerenciador de contexto
with SimpleXMLRPCServer(('localhost', PORT)) as servidor:
    # Registra as funções de inspeção system.listMethods, system.methodHelp e system.methodSignature
    servidor.register_introspection_functions()

    # Registra o método de MDC -- usa o mesmo nome para chamada da função
    servidor.register_function(mdc)

    # Deixa o servidor em loop
    print(f"Servidor ativado na porta {PORT}...\nUse Ctrl + C para deixar")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nInterrupção feita pelo teclado. Finalizando...")
        sys.exit(0)


