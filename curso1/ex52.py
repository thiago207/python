n1 = int(input('Digite seu numero inteiro e saiba se é PRIMO: '))
tot = 0

print(f'Vamos ver quais numeros seu {n1} é divisivel')
print('-'*20)

for c in range(1, n1 +1):
    
    if n1 % c == 0:
        print(f'{c} divisivel')
        tot = tot + 1
    else:
        print(f'{c}')

print(f'O numero {n1} foi divisivel {tot} vezes')

if tot == 2:
    print('Seu numero é primo!')
else:
    print(f'Ele foi dividido {tot}, logo nao é primo!')