
# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(tarefas):
    if tarefas:
        print('\nTarefas:')
        for e,v in enumerate(tarefas):
                print(f'{e+1} - {v}')
    else:
        print('Lista vazia')

def desfazer(tarefas, tarefas_refazer):
    if tarefas:
            tarefa = tarefas.pop()
            print(f'{tarefa=} removida da lista de tarefas.')
            tarefas_refazer.append(tarefa)        
    else:
            print('Lista vazia')

def refazer(tarefas, tarefas_refazer):
    if tarefas_refazer:
            tarefa = tarefas_refazer.pop()
            print(f'{tarefa=} adicionada a lista de tarefas.')
            tarefas.append(tarefa)
    else:
        print('Nada para refazer')

lista_main = []
tarefas_refazer = []

while True:
    print('COMANDOS : listar / refazer / desfazer')

    opc = input('Digite uma tarefa ou comando: ')
    comando = opc.upper().strip()
    
    if comando == 'LISTAR':
        listar(lista_main)

    elif comando == 'DESFAZER':
        desfazer(lista_main, tarefas_refazer)
        
            
    elif comando == 'REFAZER':
        refazer(lista_main, tarefas_refazer)

    else:
         lista_main.append(opc) 
 

    print()
    print(*lista_main, sep='\n')
    print()