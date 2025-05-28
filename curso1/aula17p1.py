'''num = [2,5,9,1]
#Listas sao mutaveis
num[2]= 0
num.append(10)
num.sort(reverse=True)
num.remove(2)
num.pop(3)

num.insert(2, 0) 
if 5 in num:
    num.remove(5)
else:
    print('Nao tem 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei os valores {v}')

