import os
def arqCreat():
        try:
            arquivo = open('cursoEmVideo','w')
            arquivo.close()
        except:
            print('Erro!! use: texto!')



def arqWrite(nomeAquivo ='cursoEmVideo',texto='fulano123'):
        try:
            with open(nomeAquivo,'a') as arquivo:
                arquivo.write(texto)
                print('Registrado!')

        except:
            print('Erro!! use: texto!')



def arqRead(nomeAquivo ='cursoEmVideo'):
        try:
            with open(nomeAquivo,'r') as arquivo:
                return arquivo.read()
        except:
            print('Erro!! use: texto!')


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
