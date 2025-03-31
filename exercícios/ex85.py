'''numeros = []
par = []
impar = []

for c in range(7):
    numeros.append(int(input(f'Numero {c+1}: ')))
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
print(f'Os valores digitados foram: {numeros}')
print(f'Os numeros pares em ordem crescente: {par}')
print(f'Os numeros imapres em ordem decrescente: {impar}')'''

numeros = [[], []]
valor = 0
for c in range (7):
    valor = int(input(f'Numero {c+1}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores digitados foram: {numeros}')
print(f'Os numeros pares em ordem crescente: {numeros[0]}')
print(f'Os numeros imapres em ordem decrescente: {numeros[1]}')

