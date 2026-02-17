abre = fecha = 0
expresão = str(input('Digite uma expresão: '))
for i in range(0,len(expresão)):
    if expresão[i] == '(':
        abre += 1
    if expresão[i] == ')':
        fecha += 1
print('A expressão está correta' if abre == fecha else 'A expressão está errada')