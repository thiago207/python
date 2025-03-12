n = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:  
    n1 = int(input('Digite um numero de 1 a 10: '))
    if 1 <= n1 <=10:
        break
    print('Tente novamente...!')
print(f'Seu numero {n[n1]}')
