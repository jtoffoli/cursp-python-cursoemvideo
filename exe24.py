frase = str(input('digite uma frase qualquer: ')).strip()
print('a primeira letra "a" apareceu na posição: {}'.format(frase.lower().find('a')+1))
print('a última letra "a" apareceu na posição: {}'.format(frase.lower().rfind('a')+1))
print('a letra "a" apareceu {} vezes na frase'.format(frase.lower().count('a')))