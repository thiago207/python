pessoa = {}
galera = []
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessas cadastradas. ')
media = soma / len(galera)
print('-'*40)
print(f'A media de idade é {media:.1f}')
print('-'*40)
print('As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']}')
print()
print('-'*40)
print('Lista das pessoas que estao com a idade acima da media: ')
for p in galera:
    if p['idade'] > media:
        for k,v in p.items():
            print(f'{k} = {v}')
