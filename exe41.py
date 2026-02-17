num = int(input('digite um número qualquer: '))
print('''escolha a base de conversão
[1] binário: 
[2] octal: 
[3] hexadecimal: ''')
opção = int(input('sua opção: '))
if opção == 1:
    print(f'o número convertido pra binário é: {bin(num)}')
elif opção == 2:
    print(f'o número convertido para octal é: {oct(num)}')
elif opção ==3:
    print(f'o número convertido para hexadecimal é: {hex(num)}')
else:
    print('opção inválida')
