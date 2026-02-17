def notas(*n,sit=False):
    '''
    --> Esta função pode ser usada para ver a média e a situação
    de alunos utilizando suas notas.
    :param n: Quantidade de notas para se calcular a média (Aceita vários valores)
    :param sit: Se a situação for 'True' o retorno terá a situação do aluno dependendo da média (Parâmetro opcional)
    :return: Retorna as notas, a média e a situação do aluno.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

resp = notas(4.5,10,6,7.5,sit=True)
print(f'Foram informados {resp["total"]} notas, A maior é {resp["maior"]}, A menor é {resp["menor"]} e a média é {resp["media"]:.2f} '+(f'e a sitação é {resp["situacao"]}'if "situacao" in resp else ''))
