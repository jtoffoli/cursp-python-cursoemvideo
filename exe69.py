print('-'*30)
print('LOJAS SUPER BARATÃO!')
print('-'*30)
total = qtd = cont =0
nome = ''
while True:
    nomep = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço:R$ '))
    opção = str(input('Quer continuar?[S/N]  ')).strip().upper()[0]

    if opção in 'Ss':
        cont += 1
        if preço > 1000:
            qtd += 1
        elif cont == 1:
            barato = preço
            nome = nomep
        else:
            if preço < barato:
                nome = nomep
        total += preço
    elif opção in 'Nn':
        total += preço
        if preço > 1000:
            qtd += 1
        print('Programa encerrado')
        break
    else:
        print('Opção inválida. Tente novamente.')
print('-'*15,'FIM DO PROGRAMA','-'*15)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtd} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} custando R${barato:.2f}')
