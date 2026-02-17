import math
angulo = float(input('digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o seno de {} é {:.2f}'.format(angulo, seno))
print('o cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('a tangente de {} é {:.2f}'.format(angulo, tangente))