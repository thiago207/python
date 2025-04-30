def mul(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

n1 = mul(1,2,3,4,5)
print(n1)

def imparoupar(n=None):
    try:
        if n is not None:
            if n % 2 == 0:
                return f'SEU VALOR {n} é par'
            return f'SEU VALOR {n} é impar'
        else:
            print('DIGITE ALGO VALIDO')
    except:
         print('erro')

print(imparoupar(1.5))