def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro "{entrada}" é invalidado')
        else:
            valido = True
            return float(entrada)
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

def leiaFloat(msm):
    valido = False
    while not valido:
        entrada = str(input(f'{msm}'))
        if entrada == '':
            entrada = '0'
            print('\033[31mO usuário preferiu não digitar\033[0m')
        try:
            entrada = float(entrada)
        except:
            print('\033[31mErro, Digite um valor real válido\033[0m')
        else:
            return entrada
            break
