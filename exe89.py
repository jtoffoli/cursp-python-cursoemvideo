from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)
}
for k,v in dados.items():
    print(f'o {k} tirou {v}.')
    sleep(1)
ranking = sorted(dados.items(), key = itemgetter(1), reverse=True)
for j,r in enumerate(ranking):
    print(f'{j+1}° lugar: {r[0]} com {r[1]}.')
    sleep(1)