lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado.')
    opção = str(input('Quer continuar[S/N]: ')).strip().lower()[0]
    if opção == 'n':
        break
    elif opção not in 'ns':
        print('Opção invalida, tente novamente.')
        while opção not in 'ns':
            opção = str(input('Quer continuar[S/N]: ')).strip().lower()[0]
            if opção == 'n':
                break
lista.sort()
print(f'Sua lista ficou assim: {lista}.')