import sys
import xmlrpc.client

# Função para validar entrada


def validar_entrada_input(texto_string, interruption_key='q'):
    if texto_string == interruption_key:
        print("Saindo...")
        sys.exit(-1)

    entrada = input(texto_string)

    if entrada.isdigit():
        return int(entrada)
    else:
        entrada = input('Digite um valor inteiro válido\n')
        return validar_entrada_input(entrada)


# Cria um objeto para representar nosso servidor
url_servidor = 'http://localhost:8000'
servidor = xmlrpc.client.ServerProxy(url_servidor)

# Inspeção dos métodos existentes
print("Métodos:", servidor.system.listMethods(), end="\n\n")

# Faz chamada ao servidor e obtém nosso resultado
while True:
    a = validar_entrada_input("Digite um valor inteiro ou 'q' para sair:\n")
    b = validar_entrada_input("Digite o segundo valor:\n")

    print("Resultado:", servidor.mdc(a, b))  # Dicionário
    print()
