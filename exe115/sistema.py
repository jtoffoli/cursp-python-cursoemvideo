from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep

from exe115.lib.interface import leiaint

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        #listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até logo.')
        break
    else:
        cabecalho('Opção inválida, digite novamente.')
    sleep(1)