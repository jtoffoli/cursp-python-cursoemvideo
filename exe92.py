pessoas = list()
pessoa = dict()
mulheres = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().lower()[0]
    while pessoa['sexo'[0]] not in 'mf':
        print('ERRO! Digite um sexo válido.')
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().lower()[0]
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa['nome'])
    pessoas.append(pessoa.copy())
    opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while opção not in 'sn':
        print('Opção inválida tente novamente.')
        opção = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if opção[0] == 'n':
            break
    if opção[0] == 'n':
        break
print('=-'*30)
print(f'O grupo tem {len(pessoas)} pessoas.')
print(f'A média de idade é de {soma/len(pessoas):.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m, end=' ')
print('\nLista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > soma/len(pessoas):
        print(p['nome'], end='; ')
        print(p['idade'], end='; ')
        print(p['sexo'].upper(), end='; ')
    print('\n')
print('<<ENCERRADO>>')