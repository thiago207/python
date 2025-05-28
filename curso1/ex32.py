
ano = int(input('Digite seu ano e veja se é BISSEXTO: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O {ano} é BISSEXTO!')
else:
    print(f'O {ano} nao é BISSEXTO!')
