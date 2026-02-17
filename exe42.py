from random import randint
from time import sleep
lista = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('vamos brincar jokempô')
jogador = int(input('''[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura
escolha uma opcção: '''))
print('jO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-='*15)
print(f'o computador escolheu: {lista[computador]}')
print(f'o jogador escolheu: {lista[jogador]}')
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida')
