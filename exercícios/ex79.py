lista = []
while True:
    n = (int(input(f'Digite seu numero: ')))
    if n not in lista:
        lista.append(n)
        print('Numero adicionado')
    else:
        print('Numeros iguais nao adiciono!')
    prox = str(input('Quer continuar? [S/N] ')).upper()
    if prox == 'N':
        break
lista.sort()
print(f'{lista}')
