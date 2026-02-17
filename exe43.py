
reta1 = float(input('digite o comprimento da reta 1: '))
reta2 = float(input('digite o comprimento da reta 2: '))
reta3 = float(input('digite o comprimento da reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('os seguimentos de reta podem formar um triângulo ',end='')
    if reta1 == reta2 == reta3:
        print('equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('os seguimentos de reta não podem formar um triângulo.')