import os
import time
def clear():
    if os.name =='posix':
        os.system("clear")
    elif os.name =="nt":
        os.system("cls")
    else:
        print("\n"*100)
def Menu():
    while True:
        print(f'Menu Principal')
        print(f'\033[93m1 - \033[0m \033[94mVer Pessoas cadastradas\033[0m')
        print(f'\033[93m2 - \033[0m \033[94mCadastrar nova Pessoa\033[0m')
        print(f'\033[93m3 - \033[0m \033[94mSair do Sistema\033[0m')
        resposta = input('\033[92mSua Opção: \033[0m')
        try:
            resposta = int(resposta)
            if resposta == 1:
            elif resposta == 2:
            elif resposta ==3:
            elif resposta <= 3:
                break
            else:
                clear()
                print('\033[91mErro: porfavor digite um número Dispnível no Menu \033[0m')
                time.sleep(1.2)

        except:
            print('\033[91mErro: porfavor digite um número Inteiro válido! \033[0m')





