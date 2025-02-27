from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
if idade <= 9:
    print(f'com {idade} é MIRIM!')
elif 9 < idade <= 14:
    print(f'Com {idade} é INFANTIL!')
elif 14 < idade <= 19:
    print(f'Com {idade} é JUNIOR!')
elif 19 < idade <=25:
    print(f'Com {idade} é SENIOR!')
else:
    print(f'Com {idade} é MASTER')