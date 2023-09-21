import moeda

p = float(input('digite o preco : '))

print(f'A metade = {moeda.metade(p,True)}')
print(f'o dobro é  = {moeda.dobro(p,True,"US")}')
print(f'aumentando 10% = {moeda.aumentar(p,10,True)}')
print(f'diminuendo 15% = {moeda.diminuir(p,15, True)}')