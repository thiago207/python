lista = []
pessoas = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    pessoas.append(lista[:])
    lista.clear()
    opcao = input('Quer continuar? [s/n] ').upper()
    if opcao == 'N':
        break
print(f'Foram cadastradas {len(pessoas[0])} pessoas')
print(f'O maior peso foi de {maior}')
for p in pessoas:
    if p[1] == maior:
        print(f'De: {p[0]}')
print(f'O menor peso foi de {menor}')
for p in pessoas:
    if p[1] == menor:
         print(f'De: {p[0]}')

        
