from random import randint
from time import sleep
num = randint(0, 10)
cont = 1
print('\033[35m-=-\033[m'*20)
print('\033[1;32mcomputador: pensei em um número de 0 a 5, tente adivinhar qual é...\033[m')
print('\033[35m-=-\033[m'*20)
escolha = int(input('tente adivinhar o número que o computador escolheu: '))
while escolha != num:
    print('\033[1;31mPROCESSANDO...\033[m')
    sleep(2)
    cont += 1
    if escolha > num:
        print('\033[4;36mvoçê errou, o número é menor!\033[m')
        escolha = int(input('tente adivinhar o número que o computador escolheu: '))
    else:
        print('\033[4;36mvoçê errou, o número é maior!\033[m')
        escolha = int(input('tente adivinhar o número que o computador escolheu: '))
else:
    print(f'\033[4;36mVoçê acertou depois de {cont} tentativas\033[m')