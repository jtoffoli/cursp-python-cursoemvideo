jogador = dict()
aproveitamento = list()
jogador['nome'] = str(input('Qual o nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na patida {p+1}: '))
    aproveitamento.append(gols)
jogador['gols'] = aproveitamento[:]
jogador['total'] = sum(aproveitamento)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')