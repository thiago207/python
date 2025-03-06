cont = 0
n = 0
soma = 0
n = int(input('Digite seu numero: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite seu numero: '))
print(f'voce digitou {cont} e a soma entre eles é: {soma}')
