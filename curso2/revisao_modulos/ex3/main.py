import funcoes

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('LISTA PADRAO')
funcoes.mostrar(produtos)
print()

print('LISTA COM 10% DE AUMENTO NOS PREÇOS')
aumento = funcoes.aumentar_valores(produtos)
funcoes.mostrar(aumento)
print()

print('PRODUTOS EM ORDEM DESCRESENTE')
produtos_ordenados = funcoes.ordenar_produtos_por_nome_decrescente(produtos)
funcoes.mostrar(produtos_ordenados)
print()

print('PRODUTOS EM ORDEM CRESENTE')
produtos_crescente = funcoes.ordenar_produtos_por_nome_crescente(produtos)
funcoes.mostrar(aumento)
print()

print('PRECO POR ORDEM DESCRESENTE')
produtos_por_preco = funcoes.produtos_por_preco(produtos)
funcoes.mostrar(produtos_por_preco)