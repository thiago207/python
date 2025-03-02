from datetime import date

anoatual = date.today().year
cont = 0
cont1 = 0

for c in range(1,8):
    nasc = int(input(f'Digite seu ano de nascimento {c}: '))

    idade = anoatual - nasc

    if idade >=18:
        print('Maior de idade')
        cont = cont + 1
    else:
        print('Menor de idade')
        cont1 = cont1 + 1
print(f'{cont} ja sao MAIOR de idade.')   
print(f'{cont1} sao MENOR de idade.')    

