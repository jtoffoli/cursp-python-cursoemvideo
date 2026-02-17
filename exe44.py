print('='*10,'LOJAS JT','='*10)
preço = float(input('qual o total da compra?'))
forma=int(input('''
[1] á vista dinheiro ou cheque
[2] á vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão
qual a forma de pagamento? '''))
if forma == 1:
    desconto = preço/100*10
    print(f'á vista sua compra de {preço} sairá por {preço - desconto:.2f}')
elif forma == 2:
    desconto = preço/100*5
    print(f'á vista no cartão sua compra de {preço} sairá por {preço - desconto:.2f}')
elif forma == 3:
    desconto = 0
    print(f'sua compra de {preço} será parcelada em 2x de {preço/2}')
elif forma == 4:
    parcelas = int(input('em quantas parcelas irá pagar a conta? '))
    juros = preço/100*20
    print(f'sua compra de {preço} terá {parcelas} parcelas de {(preço+juros)/parcelas:.2f},ocorreu juros de R$ {juros:.2f}')
else:
    print('opção invalida')