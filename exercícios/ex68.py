from random import randint
print('-=-' *20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' *20)
v = 0
while True:
    computador = randint(1, 10)

    jogador = int(input('Digite um valor: '))
    valor = str(input('Par ou Impar? [I / P] ')).upper().strip()[0]

    total = jogador + computador
    print('-' *40)
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print(f'DEU PAR'if total % 2 ==0 else 'DEU IMPAR')
    print('-' *40)
    if valor == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    if valor == 'I':
        if total % 2 ==1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    print('Vamos jogar novamente!')
print(f'Game over! Voce venceu {v}')