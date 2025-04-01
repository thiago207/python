lista = []
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Qual a media de {aluno['nome']}: '))
lista.append(aluno)

for a in lista:
    for k,v in a.items():
        print(f'{k} é igual a {v}')
if aluno['media'] >=7:
    print('Aprovado')
else:
    print('Reprovado')
