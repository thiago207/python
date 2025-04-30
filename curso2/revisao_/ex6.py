def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(numero)
    return print(f'---{total}---')
    
n=soma(1,2,3,4)


n1= soma(2,4,5,6,4,3,1)

numeros = (1,2,3,4,5,6,7,8,9)
soma(*numeros)