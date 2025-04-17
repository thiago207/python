def dobro(n=0,format=False):
    res = n * 2
    return res if format is False else money(res)

def metade(n=0,format=False):
    res=  n / 2
    return res if format is False else money(res)

def aumentar10(n=0,taxa=0,format=False):
    d10 = n * taxa / 100
    res = d10 + n
    return res if format is False else money(res)

def diminuir13(n=0,taxa=0,format=False):
    d13 = n * taxa / 100
    res = n - d13
    return res if format is False else money(res)

def money (n=0,moeda= 'R$'):
    return f'{moeda} {n:.2f}'.replace('.',',')

def resumo(v,a=10,r=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'PREÇO ANALISADO:  \t{money(v)}')
    print(f'DOBRO DO PREÇO:  \t{(dobro(v,True))}')
    print(f'METADE DO PRECO:  \t{(metade(v,True))}')
    print(f'{a}% de aumento:  \t{aumentar10(v,a,True)}')
    print(f'{r}% de reducao:  \t{diminuir13(v,r,True)}')
    print('-'*30)

