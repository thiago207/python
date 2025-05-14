
produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
print(*produtos, sep='\n')
soma_geral = sum(p['preco'] for p in produtos)
print('soma geral',soma_geral)

print()
produtos_acima_de_7 = [
    {**p} for p in produtos
    if p['preco'] > 7
]
soma = sum( p['preco'] for p in produtos
           if p['preco'] > 7
           )

print(*produtos_acima_de_7, sep='\n')
print('soma valores acima de 7:',soma)

lista_filtrada = [
    {**p} for p in produtos
    if p['nome'] in 'Produto 5'  'Produto 4'

]
print(*lista_filtrada, sep='\n')
total = sum( p['preco'] for p in produtos
        if p['nome'] in 'Produto 5'  'Produto 4')
            
print('soma dos produtos 4 e 5:',total) 