termo = int(input('digite o primeiro termo da razão: '))
razão = int(input('digite a razão da PA: '))
décimo = termo+(10-1)*razão
for i in range(termo,décimo + razão,razão):
    print(i)