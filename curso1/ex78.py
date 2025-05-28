lista = []
for v in range(0,5):
    lista.append(int(input(f'Digite um valor na posicao {v}: ')))
print(lista)

m = max(lista)
mi = min(lista)

print(f'O maior valor digitado foi {m} na posicao: ')
for i, v in enumerate(lista):
    if v == m:
        print(f'{i}')

print(f'O menor valor digitado foi {mi} na posicao: ')

for i, v in enumerate(lista):
    if v == mi:
        print(f'{i}')



