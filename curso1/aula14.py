'''for c in range (1,  11):
    print(c)
print('Fim')'''

#c = 1
'''while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

#n = 1
'''while n != 0:
    n = int(input('Digite um valor: '))
print('fim')'''

#r = 'S'
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar?[S/N]: ')).upper()
print('Fim')'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 ==0:
            par = par + 1
        else:
            impar = impar + 1
 
print(f'Voce digitou {par} numeros par e {impar} impares.')