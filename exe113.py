def leiaint(msg=0):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg))
            n.isnumeric()
            valor = int(n)
            ok = True
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar nenhum valor')
            ok = True
        except Exception:
            print(f'Erro na digitação do número.Tente novamente.')
        if ok:
            break
    return valor

def leiaFloat(msg=0):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg)).replace(',', '.')
            n.isnumeric()
            valor = float(n)
            ok = True
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar nenhum valor')
            ok = True
        except Exception:
            print(f'Erro na digitação do número.Tente novamente.')
        if ok:
            break
    return valor
n1 = leiaint(f'Digite um número Inteiro:')
n2 = leiaFloat('Digite um número Real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')