nome = str(input('digite seu nome: ')).strip()
lista = nome.split()
print('seu primiero nome é: {}'.format(lista[0]))
print('seu último nome é: {}'.format(lista[len(lista)-1]))
