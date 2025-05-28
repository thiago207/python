n1 = int((input('Digite seu numero: ')))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f'Analisando seu numero: {n1}')
print(f'unidade:{u}')
print(f'dezena:{d}')
print(f'centena:{c}')
print(f'milhar:{m}')

