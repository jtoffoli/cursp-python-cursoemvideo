num = int(input('digite o número que voçê quer a tabuada: '))
i = int(input('digite qual o multiplicador da tabuada voçê quer: '))
for c in range(0,i+1):
    print('{} x {} = {}'.format(num,c,num*c))
print('fim da tabuada')