from ex117SistemaFinalizado.lib.interface import *
def arqCreate(nome):
        try:
            arquivo = open(nome,'w')
            arquivo.close()
        except:
            print('Erro!! use: texto!')



def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro {nome} adicionado !!!')
            a.close()



def arqRead(nome ='cursoEmVideo'):
        try:
           a = open(nome,'rt')

        except:
            print('Erro!! use: texto!')
        else:
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n','')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')


