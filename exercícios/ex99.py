from time import sleep
def maior(lista):
    sleep(0.5)
    print('-' * 20)
    n = len(lista)
    print(f'{lista} Foram informados {n} ao todo. ')
    print(f'O maior valor foi: {max(lista)}')

    print('-' * 20)

lista1 = [2,9,4,5,7,1]
maior(lista1)
lista2 = [4,7,0]
maior(lista2)
lista3 = [2]
maior(lista3)
lista4 = [0]
maior(lista4)
lista5= [-1,-2,-3]
maior(lista5)
