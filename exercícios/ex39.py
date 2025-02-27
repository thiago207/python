from datetime import date
atual = date.today().year
ano = int(input('Diga o ano de nascimento: '))

idade = atual - ano
hora = 18 - idade
horam = idade - 18
aldo = atual + hora
saldo = atual - horam

print(f'Voce nasceu em {ano} e tem {idade} em {atual}')
if idade == 18:
    print('Esta na hora de se alistar!!')
elif idade < 18:
    print(f'Ainda vai se alistar! daqui {hora} vai ter que se alistar. em {aldo}')
    
elif idade > 18:
    print(f'Ja passou do tempo! ja passaram {horam} anos, desde a data que devia se alistar. deveria em {saldo}')
    