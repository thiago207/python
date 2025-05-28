n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

menu = 0

while menu != 5:
    print('-=-' * 20)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NUMEROS')
    print('[ 5 ] SAIR DO PROGAMA')

    menu = int(input('-Digite qual operaçao deseja: '))
    print('-=-' * 20)
    if menu == 1:
        print(f'A soma entre {n1} e {n2} = {n1 + n2}')

    if menu == 2:
        print(f'A mutiplicaçao entre {n1} e {n2} = {n1 * n2}')

    if menu == 3:
        if n1 > n2:
            print(f'o {n1} é maior que {n2}')
        elif n1 == n2:
            print(f'{n1} é igual a {n2}')
        else:
            print(f'o {n2} é maior que {n1}')

    if menu == 4:
        print('DIGITE SEUS NOVOS VALORES')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if menu > 5:
        print('Opcao invalida. Tente novamente.')

print('Fim do progama!')
