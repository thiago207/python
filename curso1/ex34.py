salario = float(input('Digite seu salario para verificar  o reajuste: '))

if salario <=1250:
    novo = salario + (salario * 15 / 100)
else: 
    novo = salario + (salario * 10 / 100)
print(f'Seu salario foi de R${salario}, para R${novo}. ')
