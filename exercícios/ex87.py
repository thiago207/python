matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = mai = somacoluna = 0
for l in range (3):
    for c in range(3):
        n = matriz [l][c] = int(input(f'Digite um valor para {l}, {c}: '))
        if n % 2 == 0:
            somapar += n
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print(f'A soma dos valores pares é: {somapar}')
for l in range(3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')

for c in range(3):
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')
        
            