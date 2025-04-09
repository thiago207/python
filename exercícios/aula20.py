'''def soma(a,b):
    print(f'A soma entre {a} e {b} é: ')
    s = a + b 
    print(f'A soma A + B = {s}')
    

soma(a=5,b=10)
soma(8,10)'''
'''def contador(*num):
    for v in num:
        print(f' {v} ', end='')
    print(f'Foram informados {len(num)} valores.')
contador(1,7,8)
contador(1,2,3,4,5,6,7,8,9,10)'''

def dobro(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
lista = [1,3,4,2]
dobro(lista)
print(lista)
