#A Biblioteca da Faculdade Dom Bosco de Porto Alegre tem 200 livros para empréstimo
#aos alunos e professores. Fazer um programa que gerencie os empréstimos dos livros da
#biblioteca. Os códigos dos livros estão armazenados em um vetor e em outro vetor estão
#armazenadas as quantidades disponíveis de cada exemplar de livro. O programa deve:
#a) fazer a leitura do vetor de códigos de livros e do vetor de quantidade de exemplares
#(supor que não existem códigos de livros duplicados – não é necessário testar esta
#condição).
#b) procurar livros que os alunos e professores desejam retirar e verificar se há
#exemplares disponíveis. Caso haja exemplares: atualizar a quantidade disponível,
#mostrar mensagem “Retirada OK!” e informar o código do livro retirado. Caso não
#haja mais exemplares disponíveis: mostrar mensagem “Todos os exemplares deste
#livro estão retirados.”. Caso o código do livro a ser retirado não exista: mostrar
#mensagem “Código do livro inválido.” ;(supor que apenas um exemplar de livro
#possa ser levado em cada retirada)
#c) programa deve ficar pesquisando livros até que seja digitado para código de livro
#9999;
#d) quando ocorrer o término da pesquisa (entrada do código 9999), exibir os códigos
#dos livros da biblioteca e a quantidade disponível de cada livro.
#Alterar o programa acima para ficar pesquisando produtos informados até que seja
#digitado para código de produto 9999.
import random
livros = [random.randint(1, 999999999) for i in range (200) ]
quantidade = [random.randint(0,10) for c in range (200)]

while True:
    codigo = int(input('digite o código do livro que deseja: '))
    if codigo in livros:
        print('código encontrado')
    elif codigo == 9999:
        print('código de saída do vetor digitado\n programa finalizado')
        break
    else:
        print('código não encontrado')
print('código dos livros: ', livros)
print('quantidade dos livros: ',quantidade)