def escreva(msg):
    
    for m in msg:
        print('-',end='')
    print()
    print(f'{msg}')
    for m in msg:
        print('-',end='')
    print()
escreva('Gustavo Guanabara')
escreva('Oi')

#Minha resolucao. A DE CIMA

def escreva(msg):
    t = len(msg) + 4
    print('-'* t)
    print(f'  {msg}')
    print('-' * t)

escreva('Gustavo Guanabara')
escreva('Oi')
    