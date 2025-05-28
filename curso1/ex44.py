preco = float(input('Preço das compras: '))
print('[ 1 ] á vista no dinheiro/cheque')
print('[ 2 ] á vista cartao ')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')

op1 = int(input('Qual a opçao de compra? '))

avistadinheiro = preco - (preco * 10 / 100)

avista = preco - (preco * 5 / 100)

juros = preco + (preco * 20 / 100) 


if op1 == 4:
    parcelas = int(input('Quantas parcelas? ')) 

    jurosparcela =  juros / parcelas
    valorp = preco / parcelas
    print(f'Sua compra sera parcelada em {parcelas} de {valorp} COM JUROS de 20% do preco total')
    print(f'Que vai de {preco} para {juros} e parcelas de {jurosparcela}')

elif op1 == 1:
    print(f'Sua compra de {preco} a vista em dinhero tem DESCONTO DE 10%')
    print(f'Que vai de {preco} paea {avistadinheiro}')

elif op1 == 2:
    print(f'Sua compra de {preco} a vista no cartao tem DESCONTO DE 5%')
    print(f'Que vai de {preco} para {avista}')

elif op1 == 3:
    parcelas = 2
    valorp = preco / parcelas
    print(f'Sua compra de {preco} em 2x de {valorp} no cartao tem preco normal sem descontos')

else:
    print('Opcao invalida, tente novamente.')

  