print('IMC')
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (altura**2)
print(f'{imc:.2f}')

if imc <=18.5:
    print('Abaixo do peso')
elif imc <=25:
    print('Peso ideal')
elif imc <=30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')