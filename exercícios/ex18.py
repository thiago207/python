from math import radians,  sin, cos, tan
angulo = float(input('Digite seu angulo: '))
r = radians(angulo)
sen = sin(r)
co = cos(r)
tg = tan(r)
print(f'O seno é: {sen:.2f}')
print(f'O cos é {co:.2f}')
print(f'A tg é: {tg:.2f}')