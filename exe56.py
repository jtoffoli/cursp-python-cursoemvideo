sexo = str(input('Digite o seu sexo [F/M]: ')).upper()[0].strip()
while sexo[0] != 'M' and sexo[0] != 'F':
    print('opção inválida')
    sexo = str(input('Digite o seu sexo novamente[F/M]: ')).upper()
else:
    print('Sexo válido')