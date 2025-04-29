lista_compras = []

while True:
    print('SELECIONE UMA OPCAO')
    opc = input('[I]INSERIR  [A]APAGAR [L]LISTAR: ').upper().strip()
    if opc == 'I':
        add = lista_compras.append(input('DIGITE A COMPRA: ' ))
    elif opc == 'A':
        for k,v in enumerate(lista_compras):
            print(f'{k} - {v}')
        try:
            remov = int(input(f'ESCOLHA O INDICE PARA APAGAR:  '))
            if  remov <= len(lista_compras):
                removido = lista_compras.pop(remov)
                print(f'"{removido}" foi removido da lista.')
        except:
            print(f'DIGITE UM VALOR VALIDO')
    elif opc == 'L':
        if not lista_compras:
            print('LISTA VAZIA.')
        else:
            print('\nLISTA DE COMPRAS:')
            for k, v in enumerate(lista_compras):
                print(f'{k + 1} - {v}')


    else:
        print('OPCAO INVALIDA')  
