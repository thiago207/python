print('-'*30)
n1 = int(input('Digite seu numero: '))
print('-'*30)
print('[  1  ] converter para BINÁRIO')
print('[  2  ] converter para OCTAL')
print('[  3  ] converter para HEXADECIMAL')
print('-'*30)
opcao = int(input('Sua opçao: '))

b = bin(n1)[2:]
o = oct(n1)[2:]
h = hex(n1)[2:]

if opcao == 1:
    print(f'Seu numero {n1} em BINÁRIO fica: {b}')

elif opcao == 2:
    print(f'Seu numero {n1} em OCTAL fica: {o}')

elif opcao == 3:
    print(f'Seu numero {n1} em HEXADECIMAL fica: {h}')
    
else:
    print('Digite um numero de 1 a 3.')
       
