#Alterar o programa acima para ficar pesquisando produtos informados até que seja
#digitado para código de produto 9999.
import random
vetor = [random.randint(1, 999999999) for i in range (100) ]
print(vetor)
while True:
    codigo = int(input('digite o código do produton que deseja comprar: '))
    if codigo in vetor:
        print('código encontrado')
    elif codigo == 9999:
        print('código de saída do vetor digitado\n programa finalizado')
        break
    else:
        print('código não encontrado')
