lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
    if opção[0] == 'n':
        break
    elif opção not in 'sn':
        print('Opção inválida. Tente novamente.')
        while opção not in 'sn':
            opção = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
            if opção[0] == 'n':
                break
print(f'Voçê digitou {len(lista)} elementos.')
print(f'A lista na ordem decrescente é:',end='')
lista.sort(reverse =True)
print(lista)
print('O valor 5 está na lista' if 5 in lista else 'O valor 5 não está na lista')
