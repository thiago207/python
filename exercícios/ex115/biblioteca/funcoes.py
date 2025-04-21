def linhas(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)

def leiaint(msg):

    while True:
        try:
            valor = int(input(msg).strip())
        except:
            print(f'Nao é um numero inteiro!')
        else:
            return valor
    

def menu(lista):
    linhas('MENU PRINCIPAL')
    c= 1
    for itens in lista:
        print(f'{c} - {itens}')
        c +=1 
    print('-'*30)
    opc = leiaint('Sua Opçao: ')
    return opc

