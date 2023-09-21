import funcaoes as fc
preco = input('Digite o preço!: ')
print(f'A metade é {fc.metade(preco)}')

print(f'aumentando 10  {fc.aumentar(preco,10)}')
print(f'A metade é {fc.diminuir(preco,taxa=15)}')