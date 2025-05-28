from random import randint
numeros = []
def sorteio(ale):
    for n in range (5):
        numeros.append(randint(0,10))
    print(f'Sorteando os 5 valores da lista: {ale} PRONTO!')
sorteio(numeros)
def par(n):
    contp=0
    conti=0
    for numero in n:
        if numero % 2 == 0:
            contp += numero
        else:
            conti += numero
    print(f'Somando os valores PARES de {numeros}, temos {contp}. E {conti} IMPARES')
par(numeros)