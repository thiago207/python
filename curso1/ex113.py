def leiaint(msg):

    while True:
        try:
            valor = int(input(msg).strip())
        except:
            print(f'Nao é um numero inteiro!')
        else:
            return valor
    
def leiareal(msg):
    
    while True:
        try:
            valor = float(input(msg).strip().replace(',','.'))
        except:
            print(f'Nao é um numero real!')
        else:
            return valor

n = leiaint('Digite um numero: ')
r = leiareal('Digite um numero real: ')
print(f'Voce digitou {n} e {r}')