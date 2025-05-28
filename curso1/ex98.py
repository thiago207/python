def contagem(i,f,p): 
    if p < 0:
        p *= -1
    if p == 0:
        p= 1   
    print(f'CONTAGEM DE {i} ate {f} DE {p} em {p}')
    
    if i < f: 
        cont = i
        while cont <= f:
            print(f'{cont+1} ', end='')
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('fim')

contagem(1,10,2)
contagem(10,0,2)
print('SUA VEZ')
contagem(int(input('INICIO: ')), int(input('FIM: ')),int(input('PASSO: ')))

'''from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
        sleep(0.5)
    print()




contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))'''


