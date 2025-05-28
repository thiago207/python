from datetime import datetime
pessoa = {}
lista = []
pessoa['nome'] = str(input('Nome: '))

nasc = int(input('Ano de nascimento: '))

pessoa['idade'] = datetime.now().year - nasc

pessoa['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))

if pessoa['ctps'] != 0:
    pessoa['contrataçao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salario: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrataçao'] + 35) - datetime.now().year)

lista.append(pessoa)

print('-=-' *20)
print(pessoa)

for k,v in pessoa.items():
    print(f'{k} tem o valor de {v}')




