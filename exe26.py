from random import randint
from time import sleep
num = randint(0, 5)
print(num)
print('\033[35m-=-\033[m'*20)
print('\033[1;32mcomputador: pensei em um número de 0 a 5, tente adivinhar qual é...\033[m')
print('\033[35m-=-\033[m'*20)
escolha = int(input('tente adivinhar o número que o computador escolheu: '))
print('\033[1;31mPROCESSANDO...\033[m')
sleep(3)
if escolha == num:
    print('\033[4;36mvoçê acertou!\033[m')
else:
    print('\033[4;36merrou, tente novamente\033[m')