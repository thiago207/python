from random import randint
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5....')
print('-=-' * 20)

ale = randint(0,5)

n1 = int(input('Adivinhe o numero de 0 a 5: '))

if n1 == ale:
    print('Acertou! me venceu :(')
else:
    print(f'Errou!! eu pensei no {ale} e nao no {n1}')
