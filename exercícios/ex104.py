''''def leiaint(int):
    valor = int.strip()
    while True: 
        if valor.isnumeric():
            print(f'Voce digitou {n.strip()}')
        else:
            print('ERRO!! digite um numero inteiro.')
    return valor 




n = (input('Digite seu numero: '))
print(leiaint(n))
'''

def leiaint(msg):
    ok = False 
    while True:
        valor = input(msg).strip()
        if valor.isnumeric():
            ok = True
        else:
            print(f'ERRO! digite um numero inteiro. ')  
        if ok:
            break      
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce digitou {n}')

'''def leia_int(solicitação):
    while True:
        n = input(solicitação)
        if n.isnumeric():
            break
        else:
            print('\033[1;31m[ERRO] Digite um número inteiro.\033[m')
    return n


n = leia_int('Digite um Número: ')
print(f'Você acabou de informar o número {n}.')'''