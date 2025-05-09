import copy

def mostrar(lista):
    for e in lista:
        print(e)
    

def aumentar_valores(lista):
    novos_produtos = copy.deepcopy(lista)
    for e in novos_produtos:
        porcentagem = e['preco'] * 10 / 100
        e['preco'] = porcentagem + e['preco']
    for p in novos_produtos:
        print(p)

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