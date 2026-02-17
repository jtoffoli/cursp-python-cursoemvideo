sair = 0
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
while sair != 5:
    opção = int(input('''
    Digite a opção desejada
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Maior
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa\nR:'''))
    if opção == 1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        mult = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print(f'dentre os valores {n1} e {n2}, {maior} é maior.')
        elif n2 > n1:
            maior = n2
            print(f'dentre os valores {n1} e {n2}, {maior} é maior.')
        else:
            print('Os valores são iguais!')
    elif opção == 4:
        print('\033[1;31mVoçê optou por digitar novos valores\033[m')
        n1 = int(input('digite um valor: '))
        n2 = int(input('digite outro valor: '))
    elif opção == 5:
        print('Voçê saiu do programa!')
        sair = 5
    else:
        print('Opção inválida')