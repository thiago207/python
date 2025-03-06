resp = 'S'
media = quant = soma = 0
while resp in 'Ss':
    num = int(input('Digite seu numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} e a media foi {media:.2f}')
print(f'O maior foi {maior} e o menor foi {menor}')