import copy

def mostrar(lista):
    for e in lista:
        print(e)
    

def aumentar_valores(lista):
    novos_produtos = copy.deepcopy(lista)
    for e in novos_produtos:
        porcentagem = e['preco'] * 10 / 100
        e['preco'] = round(porcentagem + e['preco'], 2)
    return novos_produtos

def ordenar_produtos_por_nome_decrescente(lista_produtos):
    def obter_nome(produto):
        return produto['nome']

    produtos_copiados = copy.deepcopy(lista_produtos)

    produtos_copiados.sort(key=obter_nome, reverse=True)
    
    return produtos_copiados

def ordenar_produtos_por_nome_crescente(lista_produtos):
    def obter_nome(produto):
        return produto['nome']

    produtos_copiados = copy.deepcopy(lista_produtos)

    produtos_copiados.sort(key=obter_nome)
    
    return produtos_copiados

def produtos_por_preco(lista):
    nova_lista = copy.deepcopy(lista)
    nova_lista.sorted(key=lambda e: e['preco'])
    return nova_lista
