# Importa as funções e classes necessárias dos módulos locais
from ex116minhasolução.lib.interface import *
from ex116minhasolução.lib.functions import *

# Importa as bibliotecas time e os para uso posterior
import time
import os

# Verifica se a pasta 'cursoEmVideo' já existe
if not os.path.exists('cursoEmVideo'):
    # Se não existir, cria a pasta usando a função arqCreat()
    arqCreat()

# Mensagem de confirmação de criação da pasta
print('arquivo cursoEmVideo criado com sucesso!!')

# Loop principal do programa
while True:
    # Exibe o menu e captura a escolha do usuário
    resposta = menu(['Ver pessoas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Se a resposta for 1, exibe o conteúdo do arquivo usando arqRead()
        limpa()
        print(arqRead("cursoEmVideo"))

    elif resposta == 2:
        # Se a resposta for 2, permite que o usuário digite um nome e escreve no arquivo usando arqWrite()
        limpa()
        nomes = input('Digite um nome: ')
        arqWrite(texto=nome+'\n')


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
        limpa()
        break

    else:
        # Se a resposta não for válida, mostra uma mensagem de erro
        print('\033[31mErro: Digite uma Opção válida!\033[m')
        sleep(2)
