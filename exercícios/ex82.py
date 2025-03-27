lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite um numero:  ')))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
          break

for i, v in enumerate(lista):
    if v % 2 == 0:
          listapar.append(v)
    else:
          listaimpar.append(v)
      
         
print(lista)
print(listapar)
print(listaimpar)
