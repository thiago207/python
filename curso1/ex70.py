total = 0
m1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    total += preco

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    if preco > 1000:
        m1000+=1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O preço total foi: {total}')
print(f'Temos {m1000} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')