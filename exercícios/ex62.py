print('-=-' * 20)
print('Os 10 termos de uma PA')
print('-=-' * 20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o numero da sua razao: '))

cont = 0
mais = 10
total = 0
while mais != 0:
    total = total+mais
    while cont <= total:
        print(f'{primeiro} - ', end='')
        primeiro += razao
        cont += 1
    
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
    print('Pausa')
print(f'FIM o total de termos foi {total}')
    