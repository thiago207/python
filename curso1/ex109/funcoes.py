def dobro(n=0,format=False):
    res = n * 2
    return res if format is False else money(res)

def metade(n=0,format=False):
    res=  n / 2
    return res if format is False else money(res)

def aumentar10(n=0,format=False):
    d10 = n * 10 / 100
    res = d10 + n
    return res if format is False else money(res)

def diminuir13(n=0,format=False):
    d13 = n * 13 / 100
    res = n - d13
    return res if format is False else money(res)
def money (n=0,moeda= 'R$'):
    return f'{moeda} {n:.2f}'.replace('.',',')