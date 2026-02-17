from datetime import date
idade = int(input('digite o seu ano de nascimento: '))
ano = date.today().year  - idade
if ano == 18:
    print('está na hora de voçê se alistar')
elif ano < 18:
    print('falta {} anos para voçê se alistar'.format(18 - ano))
else:
    print('\033[1;31mJÀ PASSOU {} ANO(S) QUE VOÇÊ TINHA QUE SE ALISTAR\033[m'.format(ano - 18))