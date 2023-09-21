from ex116Resposta.lib.interface import *
from ex116Resposta.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas','Cadastra nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cadastra()
    elif resposta == 3:
        print('Saido do Sistema!!')
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',)
        print("\033[31mFinalizado!!\033[m")
        break
    else:
        print('\033[31mErro: Digite uma Opção válida!\033[m')
        sleep(2)