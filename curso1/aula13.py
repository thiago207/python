i = int(input('Digite o inicio: '))

f = int(input('Digite o fim: '))

p = int(input('Digite o passo: '))
for passo in range(i, f+1, p):
    print(f'{passo}')
print('Final.')
