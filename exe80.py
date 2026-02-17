lista = list()
lista1 = []
lista2 = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
    if opção[0] == 'n':
        break
    elif opção not in 'sn':
        while opção not in 'sn':
            print('Opção inválida, tente novamente.')
            if opção[0] == 'n':
                break
for i in range(0,len(lista)):
    if lista[i] % 2 == 0:
        lista1.append(lista[i])
    else:
        lista2.append(lista[i])
print(f'A lista original: {lista}')
print(f'Os números pares na lista {lista1}')
print(f'Os números ímpares da lista {lista2}')