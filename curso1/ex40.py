n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'APROVADO!{media}')
elif media < 5:
    print(f'REPROVADO!{media}')
else:
    print(f'RECUPERACAO {media}')
