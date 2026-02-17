contador = 0
media = 0
maior = 0
velho = ''
contador2 = 0
for i in range (0,4):
    nome = str(input('digite seu nome: ')).strip()
    idade = int(input('digite sua idade: '))
    sexo = str(input('digite seu sexo(M/F): ')).strip().upper()[0]
    contador = contador +1
    media += idade
    if sexo[0] == 'M' and idade > maior:
        maior = idade
        velho = nome
    if sexo[0] == 'F' and idade < 20:
        contador2 = contador2 + 1
print('a média é {}'.format(media/contador))
print('o homem mais velho é {} con {} anos'.format(velho, maior))
print('a quantidade de mulheres coom menos de 20 anos é {}'.format(contador2))