from ex116minhasolução.lib.functions import *
def leiaInt(msg):
    valido = False
    while not valido:
        entrada = str(input(f'{msg}'))
        if entrada == '':
            entrada = '0'
            print('O usuário preferiu não digitar')
        try:
            entrada = int(entrada)
        except Exception:
            print(f'\033[31mErro: por favor, digite um número inteiro válido\033[0m')
        else:
            break
    return entrada

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    for i, op in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{op}\033[m')
    print(linha())
    opc = leiaInt('Sua Opção:')
    return opc


def limpa():
    print("\n" * 100)
    print(linha())






