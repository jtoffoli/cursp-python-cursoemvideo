print('{:=^30}'.format('Banco'))
valor = int(input('qual o valor a ser sacado: R$'))
total = valor
cedula = 50
totalcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'total de {totalcedulas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break