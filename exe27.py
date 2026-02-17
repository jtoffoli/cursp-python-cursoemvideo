km = int(input('\033[31mqual a velocidade que voçê está? '))
if km <= 80:
    print('\033[36ma velocidade é permitida')
else:
    multa = (km - 80)*7
    print('\033[36mvelocidade acima do permitido, multa de {} reais'.format(multa))