lista_geral = []
media = num =cont = 0
pessoas = list()
notas = list()
n = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    for i in range(0,2):
        n.append(float(input(f'Digite o valor da {i+1}º nota: ')))
    notas.append(n[:])
    media = (sum(n)) / len(n)
    pessoas.append(nome)
    pessoas.append(media)
    lista_geral.append(pessoas[:])
    pessoas.clear()
    n.clear()
    opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if opção not in 'sn':
        print('Opção inválida tente novamente.')
        opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if opção[0] == 'n':
            break
    elif opção[0] == 'n':
        break
print('=-'*30)
for i in range(0,len(lista_geral)):
    print(f'{i+1:<4}',end = '')
    print(f'{lista_geral[i][0]:<10}', end='')
    print(f'{lista_geral[i][1]:>.1f}')
while True:
    if cont == 0:
        opção = str(input('Quer mostrar as notas de algum aluno? [S/N] ')).strip().lower()[0]
    else:
        opção = str(input('Quer mostrar mais alguma nota? [S/N] ')).strip().lower()[0]
    cont += 1
    if opção not in 'sn':
        print('Opção inválida tente novamente.')
        opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if opção[0] == 'n':
            break
    elif opção[0] == 'n':
        break
    num = int(input('Digite o número da posição que voçê quer ver: '))
    print(f'As notas de {lista_geral[num-1][0]} são {notas[num-1]}')
print(f'{'volte sempre':<^30}')
