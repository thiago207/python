from random import randint
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 10....')
print('-=-' * 20)
print('Tente advinhar')

acertou = False
palpites = 0

while not acertou:
    jogador= int(input('Qual seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
            
print(f'Acertou! Precisou de {palpites} tentativas para acertar.')