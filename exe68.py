from time import sleep
print('-'*30)
print('CADASTRE PESSOAS')
print('-'*30)
maior = 0
homem = 0
menor = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo[0] == 'M':
        homem += 1
    if sexo[0] == 'F' and idade < 20:
        menor += 1
    opção = str(input('Voçê quer continuar[S/N]: ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Voçê quer continuar[S/N]: ')).strip().upper()[0]
    if opção in 'nN':
        print('Programa finalizado')
        break
print('-='*20) 
print('\0331;31[mANALISANDO DADOS\0331;31[m')
print('-='*20)
sleep(2)
print(f'A quantidade de pessoas maiores que 18 anos é {maior}!')
print(f'A quantidade de homens cadastrados é {homem}!')
print(f'A quantidade de mulheres menores de 20 anos é {menor}!')
