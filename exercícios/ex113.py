def leiaint(msg):
    ok = False 
    while True:
        try:
            valor = int(input(msg).strip())
        except:
            print(f'Nao é um numero inteiro!')
        else:
            break
    return valor
def leiareal(msg):
    
    while True:
        try:
            valor = float(input(msg).strip().replace(',','.'))
        except:
            print(f'Nao é um numero real!')
        else:
            break
    return valor

n = leiaint('Digite um numero: ')
r = leiareal('Digite um numero real: ')
print(f'Voce digitou {n} e {r}')