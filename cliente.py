import sys
import re
import xmlrpc.client

# Função para validar entrada

def validar_entrada_input(texto, interruption_key='q'):
    entrada = None

    while True:
        try:
            entrada = re.sub("[+-]", "", input(texto))
        except KeyboardInterrupt:
            print("Interrupção via teclado. Deixando programa...")
            sys.exit(-1)

        if entrada.isdigit():
            break
        elif entrada == interruption_key:
            print("Saindo...")
            return None

        texto = 'Digite um valor inteiro válido (\'q\' para sair)\n'

    return int(entrada)


# Cria um objeto para representar nosso servidor
url_servidor = 'http://localhost:8000'
servidor = xmlrpc.client.ServerProxy(url_servidor)

# Inspeção dos métodos existentes
print("Métodos:", servidor.system.listMethods(), end="\n\n")
print("Descrição do método mdc (a ser chamado a seguir):",
      servidor.system.methodHelp('mdc'))

# Faz chamada ao servidor e obtém nosso resultado
while True:
    a = validar_entrada_input("Digite um valor inteiro ou 'q' para sair:\n")
    b = validar_entrada_input(
        "Digite o segundo valor:\n") if a is not None else None

    if b is None:
        break

    print(f"mdc({a}, {b}):", servidor.mdc(a, b))  # Dicionário
    print("-"*20)
