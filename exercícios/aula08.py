import random
from math import sqrt, floor
num = int(input('Digite seu numero: '))
ale = random.randint(1, 10)
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {floor(raiz):.2f} ale {ale}')