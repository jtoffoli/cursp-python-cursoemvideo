def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção:')
    return opc


def leiaint(msg=' '):
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