from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['CTPS'] = int(input('CTPS(0 caso não tenha): '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Qual o ano da contratação: '))
    pessoa['salário'] = float(input('qual o seu salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - date.today().year)
print('-='*30)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')