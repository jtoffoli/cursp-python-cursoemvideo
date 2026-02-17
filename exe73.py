from random import randint
tupla = (randint(0,100), randint(0,100), randint(0,100),
         randint(0,100),randint(0,100))
print(f'Valores sorteados: {tupla}')
print(f'O mair valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')