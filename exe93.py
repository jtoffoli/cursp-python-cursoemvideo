jogador = dict()
aproveitamento = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    aproveitamento.clear()
    for p in range(0, partidas):
        gols = int(input(f'Quantos gols na par tida {p+1}: '))
        aproveitamento.append(gols)
    jogador['gols'] = aproveitamento[:]
    jogador['total'] = sum(aproveitamento)
    time.append(jogador.copy())
    opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while opção not in 'sn':
        print('Opção inválida tente novamente.')
        opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if opção[0] == 'n':
            break
    if opção[0] == 'n':
        break
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4}',end='  ')
    for v in v.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*40)