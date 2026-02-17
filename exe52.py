from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(0,7):
    nascimento = int(input('digite seu ano de nascimento: '))
    if ano - nascimento >= 21:
        maior = maior+1
    else:
        menor = menor+1
print('{} pessoas já atingiram maioridade'.format(maior))
print('{} pessoas são menores de idade'.format(menor))