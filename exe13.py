import math
from math import pow
c1 = float(input('digite o valor do cateto oposto:'))
c2 = float(input('digite o valor do cateto adjacente:'))

hipotenusaQ = pow(c1, 2) + pow(c2, 2)
hipotenusa = math.sqrt(hipotenusaQ)
print('o valor da hipotenusa ao quadrado é {}, quando o cateto oposto é {}, e o cateto adjacente é{}'.format(hipotenusaQ, c1 , c2))
print('a hipotenusa arredondado e sem potência é {:.2f}'.format(hipotenusa))