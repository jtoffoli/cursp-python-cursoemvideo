cadastro = list()
pessoas = list()
while True:
    pessoas.append(str(input('nome: ')))
    pessoas.append(float(input('peso: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    opção = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if opção[0] == 'n':
        break
    elif opção[0] not in 'sn':
        print('Opção inválida, tente novamente.')
        opção = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if opção[0] == 'n':
            break
print(f'O total de pessoas cadastradas foi {len(cadastro)}')
print('faz parte do grupo dos mais pesados: ',end = ' ')
for p in cadastro:
    if p[1] >= 100:
        print(p[0], end = ' ')
print('\n')
print('faz parte do grupo dos mais leves: ', end=' ')
for p in cadastro:
    if p[1] <= 70:
        print(p[0], end = ' ')