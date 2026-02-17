tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
         'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')
while True:
    numero = int(input('Digite um número para ver sua forma extensa(0 a 20): '))
    while numero < 0 or numero > 20:
        numero = int(input('Número iválido digite novamente: '))
    print(f'voçê digitou {tupla[numero]}')
    opção = str(input('Quer continuar? [S/N]: ' )).strip().upper()[0]
    if opção == 'N':
        break
    elif opção not in 'SN':
        while opção not in 'SN':
            opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]