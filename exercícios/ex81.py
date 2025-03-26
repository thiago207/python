lista = []
while True:
    lista.append(int(input('Digite um numero:  ')))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print(f'Sua lista tem {len(lista)} elementos.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('Tem 5 na lista')
