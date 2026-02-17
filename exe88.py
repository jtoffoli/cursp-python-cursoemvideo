aluno = dict()
aluno['nome'] = str(input('nome do aluno: '))
aluno['média'] = float(input(f'Qual a média de {aluno["nome"]}: '))
print('Situação é igual a ',end='')
if aluno['média'] >= 7:
    print('aprovado')
elif 7 > aluno['média'] > 5:
    print('recuperação')
else:
    print('reprovado')
    