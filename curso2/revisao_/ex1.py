nome = input('Digite seu nome ')
idade = int(input('Digite seu nome '))
print(f'SEU NOME {nome}')
print(f'SEU NOME INVERTIDO {nome[::-1]}')
if ' ' in nome:
    print(f'SEU NOME TEM ESPAÇOS')
else:
    print(f'SEU NOME nao TEM ESPAÇOS')
print(f'SEU NOME TEM {len(nome.strip())}')
print(f'A PRIMEIRA LETRA DO SEU NOME É {nome[0]}')
