distancia = int(input('informe a distância da viagem em KMs: '))
if distancia <= 200:
    preco = distancia * 0.50
    print('o preço da viagem é {:.2f}'.format(preco))
elif distancia > 200:
    preco = distancia * 0.45
    print('o preço da viagem é {:.2f}'.format(preco))