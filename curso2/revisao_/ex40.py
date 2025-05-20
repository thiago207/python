
# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista_main = []
desfeitos = []
while True:
    print('COMANDOS : listar / refazer / desfazer')

    opc = input('Digite uma tarefa ou comando: ')
    comando = opc.upper().strip()
    
    if comando == 'LISTAR':
        print('\nTarefas:')
        if lista_main:
            for e,v in enumerate(lista_main):
                print(f'{e+1} - {v}')
        else:
            print('Lista vazia')
    elif comando == 'DESFAZER':
        if lista_main:
            desfeitos = lista_main.pop()
            print('COMANDO FEITO')
        else:
            print('erro')
    elif comando == 'REFAZER':
        if desfeitos:
            lista_main.append(desfeitos)
        else:
            print('erro')
    else:
        lista_main.append(opc)
        
    if comando not in 'LISTAR':
        print()
        print(*lista_main, sep='\n')
        print()