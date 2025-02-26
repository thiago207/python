nome = str(input('Digite seu nome: '))
t = nome.upper()



if t == 'THIAGO':

    print('Que nome lindo !!!!')
elif nome.upper() == 'JULIANA' or nome.upper() == 'JORGE':
    print('Que nome topado!')
else:
    print('nome ok.')
print(f'bom dia {nome.title()}')