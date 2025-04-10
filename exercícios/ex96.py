print('=-'*20)
print('Controle de Terrenos')

def area(l, a):
    area = l * a
    print(f'A area de um terreno ! {l} x {a} ! é de {area}m²')


l = float(input('Largura (m): '))
a = float(input('Altura (m): '))
area(l,a)

