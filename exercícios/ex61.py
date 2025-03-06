
print('-=-' * 20)
print('Os 10 termos de uma PA')
print('-=-' * 20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o numero da sua razao: '))

cont = 0
while cont <=10:
    print(f'{primeiro} - ', end='')
    primeiro += razao
    cont += 1
print('FIM')
    
