from exe115.lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o aqrquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>} anos.')
    finally:
        a.close()

def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve erro ao adicioanr os dados')
        else:
            print('Adicionado com sucesso')