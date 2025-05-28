from math import hypot
co = float(input('Digite seu cateto oposto: '))
ca = float(input('Digite seu cateto adjacente: '))
h = hypot(co, ca)
print(f'sua hipotenusa é {h:.2f}')