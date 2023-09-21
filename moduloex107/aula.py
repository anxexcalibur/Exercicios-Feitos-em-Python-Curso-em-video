
"""
 n = int(input('num'))
 ValueError: invalid literal for int() with base 10: 'oito'
 chama-se excessão  quando  o codigo ta certo porém acontece um erro!
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador'))
    r = a/b

except (ValueError, TypeError):
    print(f'Tivemos um problem com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(r)
finally:
    print('volltando aqui porra !!')

