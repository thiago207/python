l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4]

for l1,l2 in zip(l1,l2):
   print(l1, '+',l2,end=' = ')
   print(f'{l1 + l2}')


#USANDO A LOGICA SEM A FUNCAO ZIP
#lista_soma=[]
#for i in range(len(l2)):
#    lista_soma.append(l1[i] + l2[i])
#    
#print(lista_soma)