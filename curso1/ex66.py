soma = 0
cont = 0
while True:
    n = int(input('Digite seu numero [ 999 para parar ]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Voce digitou {cont} e a soma entre eles foram {soma}')