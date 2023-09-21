def aumentar(preco = 0,taxa = 0,formatado = False,sigla = 'R$'):
    res = preco + (preco* taxa/100)
    if formatado == False:
        return res
    else:
        return moeda(res,sigla)

def diminuir(preco = 0,taxa = 0, formatado = False,sigla = 'R$'):
    res = preco - (preco * taxa / 100)
    if formatado == False:
        return res
    else:
        return moeda(res,sigla)

def dobro(preco = 0, formatado = False,sigla = 'R$'):
    res = preco *2
    if formatado == False:
        return res
    else:
        return moeda(res,sigla)

def metade(preco = 0,formatado = False,sigla = 'R$'):
    res = preco /2
    if formatado == False:
        return res
    else:
        return moeda(res,sigla)

def moeda(preco = 0, moeda = 'R$'):
    return F'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco = 0, taxa = 10,taxamin = 5):
    print('='*30)
    print('Resumo'.center(30))
    print('=' * 30)
    print(f'= Diminuindo {int(taxamin)} % : {diminuir(preco,taxamin,True)}')
    print(f'= Aumentando {int(taxamin)} % : {aumentar(preco,taxa,True)}')
    print(f'= O dobro de {preco}: {dobro(preco,True)}')
    print(f'= A metade  de {preco}: {metade(preco,True)}')
    print('='*30)