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