import json

def listar(tarefas):
    print()
    if tarefas:
        for elemento, tarefa in enumerate(tarefas):
            print(f'{elemento+1}) {tarefa}')
        return 
    print('Lista vazia')

def desfazer(tarefas,tarefas_desfazer):
    if tarefas:
        tarefa_removida = tarefas.pop()
        print(f'{tarefa_removida=} removida')
        tarefas_desfazer.append(tarefa_removida)
        return
    print()
    print('Lista vazia')

def refazer(tarefas, tarefas_desfeitas):
    if tarefas_desfeitas:
        tarefa_removida = tarefas_desfeitas.pop()
        print(f'{tarefa_removida=} desfeito')
        tarefas.append(tarefa_removida)
        return
    print()
    print('NADA A DESFAZER.')

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados



def salvar(tarefas, caminho_relativo):
    dados = tarefas
    with open(caminho_relativo, 'w' , encoding='utf8') as arquivo:
        dados = json.dump(tarefas ,  arquivo, indent=2, ensure_ascii=False)
    return dados

caminho = 'treino.json'
lista_main = ler([], caminho)
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer e refazer')
    opc = input('Digite uma tarefa ou comando: ')
    comando = opc.upper().strip()

    
    if comando == 'LISTAR':
        listar(lista_main)

    elif comando == 'DESFAZER':
        desfazer(lista_main, tarefas_refazer)
        listar(lista_main)
            
    elif comando == 'REFAZER':
        refazer(lista_main, tarefas_refazer)
        listar(lista_main)
 

    else:
         lista_main.append(opc)
         listar(lista_main)
    salvar(lista_main, caminho)