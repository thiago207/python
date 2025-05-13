from itertools import combinations, permutations, product
def funcao(func):
    def print_iter(iterator, valor=None):
        if  valor is not None:
            for e in func(iterator,valor):
                print(e)
        else:
            for e in func(iterator):
                    print(e)
    return print_iter

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [['preta', 'branca'],
             ['p','m','g'],
             
             ]

fazer = funcao(combinations) #nao tem ordem (a,b)(b,c)
fazer(pessoas,2)
print(fazer)

print()

fazer = funcao(permutations) #tem ordem  ex (a,b)(a,c) 
fazer(pessoas,2)
print(fazer)

print()

fazer = funcao(product) #Gera todas as combinações possíveis com repetição permitida.

fazer(*camisetas)
print(fazer)