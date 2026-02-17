print('-='*20)
print('JOGO DE PAR OU ÍMPAR')
print('-='*20)
from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    opção = str(input('Escolha uma opção[P/I]: ')).strip().upper()[0]
    computador = randint(0,10)
    soma = computador + jogador
    while opção[0] not in 'PI':
        opção = str(input('Escolha uma opção[P/I]: ')).strip().upper()[0]
    if soma % 2 == 0:
        if opção[0] == 'P':
            vitoria += 1
            print('-' * 20)
            print(f'Voçê ganhou,o computador jogou {computador} e voçê {jogador}, portanto o resultado é {soma} um número PAR!')
            print('-' * 20)
        else:
            print('-'*20)
            print(f'Voçê perdeu,o computador jogou {computador} e voçê {jogador}, portanto o resultado é {soma} um número PAR!')
            print('-' * 20)
            break
    else:
        if opção[0] == 'I':
            vitoria += 1
            print('-' * 20)
            print(f'Voçê ganhou,o computador jogou {computador} e voçê {jogador}, portanto o resultado é {soma} um número ÍMPAR!')
            print('-' * 20)
        else:
            print('-' * 20)
            print(f'Voçê perdeu,o computador jogou {computador} e voçê {jogador}, portanto o resultado é {soma} um número íMPAR!')
            print('-' * 20)
            break
print(f'GAME OVER! Voçê venceu {vitoria} vezes')
