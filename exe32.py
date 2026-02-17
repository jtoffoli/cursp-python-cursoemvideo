from datetime import date
cores = {'amarelo' : '\033[1;33m' , 'vermelho' : '\033[1;31m', 'limpa' : '\033[m'}
ano = int(input('{}que ano quer anlisar? digte 0 para analisar o ano atual: {}'.format(cores['amarelo'],cores['limpa'])))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('{}o ano {} é bissexto{}'.format(cores['vermelho'],ano, cores['limpa']))
else:
    print('{}o ano {} não é bissexto{}'.format(cores['vermelho'],ano, cores['limpa']))