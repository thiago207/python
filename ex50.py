soma = 0
cont = 0
for c in range(1,7,):
    num = int(input('Digite seu numero: '))
    if num % 2 == 0:
        soma = soma + num 
        cont = cont + 1
print(f'A soma somente dos numeros pares {cont} é: {soma}')

 