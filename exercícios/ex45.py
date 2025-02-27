from random import randint
from time import sleep
itens = ('Pedra', 'Papel',
'Tesoura')
computador = randint(0, 2)

print('Suas opcoes: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

escolha = int(input('Qual sua jogada? '))

print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!!')

print('-=-' * 20)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador jogou {itens[escolha]}')
print('-=-' * 20)

if computador == 0:

    if escolha == 0:
       print('EMPATE!')
    elif escolha == 1:
        print('JOGADOR VENCE')
 
    elif escolha == 2:
        print('COMPUTADOR VENCE!')

    else:
        print('Jogada invalida!!')

elif computador == 1:

    if escolha == 0:
        print('COMPUTADOR VENCE!')

    elif escolha == 1:
        print('EMPATE!')

    elif escolha == 2:
        print('JOGADOR VENCE!')

    else:
        print('Jogada invalida!!')

elif computador == 2:

    if escolha == 0:
        print('JOGADOR VENCE!')


    elif escolha == 1:
        print('COMPUTADOR VENCE!')

    elif escolha == 2:
        print('EMPATE!')
        

    else:
        print('Jogada invalida!!')