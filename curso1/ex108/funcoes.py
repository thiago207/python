def dobro(n=0):
    r = n * 2
    return r

def metade(n=0):
    return n / 2

def aumentar10(n=0):
    d10 = n * 10 / 100
    aumento = d10 + n
    return aumento

def diminuir13(n=0):
    d13 = n * 13 / 100
    diminuir = n - d13
    return diminuir

def money (n=0,moeda= 'R$'):
    return f'{moeda} {n:.2f}'.replace('.',',')