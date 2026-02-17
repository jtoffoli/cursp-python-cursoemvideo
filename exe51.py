frase =  str(input('digite uma frase/palavra: ')).replace(' ','').lower()
if frase[0:] == frase[::-1]:
    print('a frase/palavra é um palíndromo')
    print('frase/palavra como voçê escreveu: {}'.format(frase[0:]))
    print('frase com a ordem inversa: {}'.format(frase[::-1]))
else:
    print('a frase/palavra não é um palíndromo')
# resolução usando for
frase =  str(input('digite uma frase/palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('é um palíndromo')
else:
    print('não é um palíndromo')
print(junto)
print(inverso)