# Importa as funções e classes necessárias dos módulos locais
from ex117SistemaFinalizado.lib.interface import *
from ex117SistemaFinalizado.lib.functions import *

# Importa as bibliotecas time e os para uso posterior
import time
import os
arq = 'cursoemvideo.txt'
# Verifica se a pasta 'cursoEmVideo' já existe
if not os.path.exists('cursoEmVideo'):
    # Se não existir, cria a pasta usando a função arqCreat()
    arqCreate(arq)
    # Mensagem de confirmação de criação da pasta
    print('arquivo cursoEmVideo criado com sucesso!!')


# Loop principal do programa
while True:
    # Exibe o menu e captura a escolha do usuário
    resposta = menu(['Ver pessoas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Se a resposta for 1, exibe o conteúdo do arquivo usando arqRead()
        print(arqRead(arq))

    elif resposta == 2:
        # Se a resposta for 2, permite que o usuário digite um nome e escreve no arquivo usando arqWrite()
        cabeçalho('NOVO CADASTRO')
        nome = input('Digite um nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        # Se a resposta for 3, sai do sistema após mostrar uma mensagem de finalização
        print('Saindo do Sistema!!')
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        print("\033[31mFinalizado!!\033[m")
        time.sleep(0.5)
        break

    else:
        # Se a resposta não for válida, mostra uma mensagem de erro
        print('\033[31mErro: Digite uma Opção válida!\033[m')
        sleep(2)
