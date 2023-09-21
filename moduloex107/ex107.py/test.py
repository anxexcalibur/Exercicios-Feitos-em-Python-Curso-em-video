import moeda

p = float(input('digite o preco : '))

print(f'A metade = {moeda.moeda(moeda.metade(p))}')
print(f'o dobro é  = {moeda.moeda(moeda.dobro(p))}')
print(f'aumentando 10% = {moeda.moeda(moeda.aumentar(p,10))}')
print(f'diminuendo 15% = {moeda.moeda(moeda.diminuir(p,15))}')