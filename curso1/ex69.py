print('-'*25)
print('  CADRASTRE UMA PESSOA')
print('-'*25)
h = 0
m = 0
m20 = 0
i18 = 0
while True:
    idade = int(input('Digite sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

    if sexo == 'M':
        h += 1
    if sexo == 'F':
        m += 1
    if sexo == 'F' and idade < 20:
      m20 += 1
    if idade >= 18:
        i18 += 1

    print('-'*25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-'*25)
    if continuar == 'N':
        break


print(f'FIM DO PRAGAMA')
print('-'*25)
print(f' {i18} PESSOAS MAIORES DE IDADE')
print('-'*25)
print(f'{h} CADRASTROS DO SEXO MASCULINO')
print('-'*25)
print(f'{m} CADRASTROS DO SEXO FEMININO, sendo {m20} com MENOS de 20 anos.')