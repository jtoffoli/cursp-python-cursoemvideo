def escreva(msg):
    print('~'*(len(mensagem)+4))
    print(f'  {msg}')
    print('~'*(len(mensagem)+4))
for i in range(0,3):
    mensagem = str(input('Digite uma mensagem: ')).strip()
    escreva(mensagem)