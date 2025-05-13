
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumenta(valor,porcentagem):
    return round(valor * porcentagem,2)

novos_produdos = [
    {**p, 'preco': aumenta(p['preco'], 1.1) } for p in produtos 

]
print_iter(novos_produdos)


#for p in produtos:
#    if p['preco'] > 20:
#        print(p)

produtos_filtrados = [
    p for p in produtos
    if p['preco'] > 20
]
print_iter(produtos_filtrados)