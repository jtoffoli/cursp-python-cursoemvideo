print('-'*30)
print('TABUADA')
print('-'*30)
while True:
    n = int(input('Voçê quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Programa tabuada encerrado')
        break
    else:
        print('-=' * 15)
        for c in range(0, 11):
            print(f'{n} x {c} = {n*c}')
        print('-='*15)