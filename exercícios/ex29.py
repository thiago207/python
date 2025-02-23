v = float(input('Qual a velocidade do carro: '))
multa = (v-80) * 7
if v >80: 
    print('Voce foi multado por estar acima dos 80km/h')
    print(f'A multa custa 7 reais por cada km acima do limite')
    print(f'Vai pagar RS{multa:.2f}')

else:
    print('Parabens! nao foi multado')