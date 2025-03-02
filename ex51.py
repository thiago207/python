print('-=-' * 20)
print('Os 10 termos de uma PA')
print('-=-' * 20)
p = int(input('Digite o primeiro termo: '))

r = int(input('Digite o numero da sua razao: '))

d = p + (10 - 1) * r

for c in range(p, d + r, r):
    print(f'{c}', end=' - ')
print('ACABOU')
    