'''pessoas = {'nome':'Thiago','sexo':'M','idade':22}
for k,v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'Sao Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''
estado = dict()
brasil = list()
for c in range(2):
    estado['uf'] = str(input('Digite a uf: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'A {k} = {v}')