import funcoes

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
funcoes.mostrar(produtos)
print()

funcoes.aumentar_valores(produtos)
print()

produtos_ordenados = funcoes.ordenar_produtos_por_nome_decrescente(produtos)
for p in produtos_ordenados:
    print(p)

print()
produtos_crescente = funcoes.ordenar_produtos_por_nome_crescente(produtos)
for e in produtos_crescente:
    print(e)

