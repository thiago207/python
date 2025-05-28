'''def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    
    """
    c = i
    while c <= f:
        print(c)
        c += p
contador(0,100,10)
help(contador)'''

'''def soma (a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = soma(10,20)
r2 = soma(8,7)
r3 = soma(8)
print(f'Meu calculos deram: {r1}, {r2}, {r3}')'''

'''def funcao(n):
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
print(f'N1 fora vale {n1}')'''
def parouimpar(num=0):
    if num % 2 ==0:
        return True
    else:
        return False
n = int(input('Digite um numero: '))
if parouimpar(n):
    print('É par')
else:
    print('É impar!')
