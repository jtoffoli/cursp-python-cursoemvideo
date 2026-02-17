cores = {'limpa' : '\033[m',
         'vermelho' : '\033[1;31m',
         'azul' : '\033[1;34m',
         'verde': '\033[1;32m',
         'roxo' : '\033[1;35m'}
reta1 = float(input('{}digite o comprimento da reta 1: {}'.format(cores['vermelho'],['limpa'])))
reta2 = float(input('{}digite o comprimento da reta 2: {}'.format(cores['azul'], ['limpa'])))
reta3 = float(input('{}digite o comprimento da reta 3: {}'.format(cores['roxo'],['limpa'])))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('{}os seguimentos de reta podem formar um triângulo.{}'.format(cores['verde'], ['limpa']))
else:
    print('{}os seguimentos de reta não podem formar um triângulo.{}'.format(cores['verde'], ['limpa']))