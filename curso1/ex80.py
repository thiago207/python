lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n < lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
                
