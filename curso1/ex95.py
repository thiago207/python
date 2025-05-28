dados = {} #DIOCIONARIO 
time = [] # LISTA 
listagols = [] # LISTA 
 
while True:
    dados.clear()

    dados['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas ele jogou? '))

    listagols.clear()

    for p in range(tot):
            listagols.append(int(input(f'     Quantos gols na partida {p+1}: ')))
    dados['gols'] = listagols[:]
    dados['total'] = sum(listagols) 
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*40)
for i in dados.keys():
     print(f'    {i:<15}', end='')
print()
for k,v in enumerate(time):
     print(f'{k:>4} ', end='')

     for d in v.values():
          print(f'{str(d):<15}', end='')   

     print()
while True:
     busca = int(input('Mostrar dados de qual jogador? (999 parar) '))
     if busca == 999:
          break
     if busca >= len(time):
          print('Erro! Nao existe jogador com esse codigo!')
     else:
          print(f' -- LEVANTAMENDO DO JOGADOR {time[busca]['nome']}')
          for i, g in enumerate(time[busca]['gols']):
               print(f'    No jogo {i+1} fez {g} gols.')
     print('-'*40)
print('FIM')  