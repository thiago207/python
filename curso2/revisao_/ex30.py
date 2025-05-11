l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4]

for l1,l2 in zip(l1,l2):
   print(l1, '+',l2,end=' = ')
   print(f'{l1 + l2}')

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]

print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
#USANDO A LOGICA SEM A FUNCAO ZIP
#lista_soma=[]
#for i in range(len(l2)):
#    lista_soma.append(l1[i] + l2[i])
#    
#print(lista_soma)