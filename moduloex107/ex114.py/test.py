from utilidadescv import moeda,dado,requests
url = 'pudim.com.br'
if dado.acessar(url):
    print(f'Conexão com {url} Bem-Sucedida.')
else:
    print(f' não foi positive conectar-se com {url}')