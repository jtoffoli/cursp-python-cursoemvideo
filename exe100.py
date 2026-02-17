def votar(num):
    from datetime import date
    ano = date.today().year
    idade = ano - num
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
n = int(input('Em que ano você nasceu?: '))
print(votar(n))