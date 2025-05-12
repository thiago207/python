'''numeros = (input('DIGITE: '))

l = numeros.split(',')
print(l)
t = tuple(l)
print(t)'''

'''from math import sqrt
numeros = (input('DIGITE: '))
v = numeros.split(',')
print(v)
lista = [ ]
for n in v:
    v = int(n)
    print(type(v))
    q = sqrt(((2 * 50* v)/ 30))
    lista.append(q)
print((lista))'''

'''lista = sorted([p for p in input().split(',')])
print(lista)
print(','.join(lista))'''

lista = [palavra for palavra in input(': :> ').split(' ')]
#print(lista)

def analisar(lista):
    verificar = set()
    for e in lista:
        verificar.add(e)
    return sorted(verificar)

v = analisar(lista)
for e in v:
    print(e,end=' ')