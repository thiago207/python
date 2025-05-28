'''from math import factorial
n = int(input('Digite um numero para calcular o fatorial: '))
f = factorial(n)
print(f'Seu numero {n} fatorial é {f}')'''
n = int(input('Digite um numero para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}',end = ' ')
    f = f * c
    c = c - 1
    print(' x ' if c >= 1 else ' = ', end='')   
print(f'{f}') 