#Uma empresa vende 100 produtos cujos códigos estão armazenados em um vetor. Fazer
#um programa que procure um produto que um cliente deseja comprar. Supor que não
#existem códigos duplicados.
import random
vetor = [random.randint(1, 999999999) for i in range (100) ]
print(vetor)
codigo=int(input('digite o código do produton que deseja comprar: '))
if codigo in vetor:
    print('código encontrado')
else:
    print('código não encontrado')