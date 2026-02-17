tupla = ('rtx 5060',2200,
        'ryzen 7 5700x' , 1100,
        'ssd nvme 1tb',400,
        'fonte msi mag 650',300,
        'water cooler rise mode',140,
        '32gb Ram',400,
        'b550m',600)
for i in range(0,len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R${tupla[i]:>.2f}')