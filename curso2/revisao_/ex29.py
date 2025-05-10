l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP','MG']

lista_nova = [f'{cidade} - {estado}' for cidade, estado in zip(l1, l2)]

print(list(zip(l1,l2)))
print()
print(lista_nova)
print()
for cidade,estado in zip(l1,l2):
    print(f'{cidade} - {estado}')
    

#def zipper(lista1,lista2):
#    maximo = min(len(l1), len(l2))
#    return [(l1[i],l2[i]) for i in range(maximo)]
#l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
#l2 = ['BA', 'SP','MG']
#print(zipper(l1, l2))