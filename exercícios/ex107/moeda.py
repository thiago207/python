import funcoes
p = float(input('Digite o preço: '))
while True:
    print('[1] METADE DO PRECO')
    print('[2] DOBRO DO PREÇO')
    print('[3] AMUMENTAR 10%')
    print('[4] DEMINUIR 13% ')
    print('~' * 30)
    opcao = (input('Qual sua opcao: '))
    while opcao not in '1234':
        print('DIGITE UM VALOR VALIDO! ')
        opcao = (input('Qual sua opcao: '))
    

    if opcao == '1':
        print(f'A metade do seu valor é {funcoes.metade(p)}')
    if opcao == '2':
        print(f'O dobro do seu valor é {funcoes.dobro(p)}')
    if opcao == '3':
        print(f'O aumento de 10% do seu valor é {funcoes.aumentar10(p)}')
    if opcao == '4':
        print(f'A reduçao de 13% do seu valor é {funcoes.diminuir13(p)}')
    
    
    continuar= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
