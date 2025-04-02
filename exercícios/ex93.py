dados = {}

listagols = []

dados['nome'] = str(input('Nome do jogador: '))

dados['partidas'] = int(input('Quantas partidas ele jogou? '))

if dados['partidas'] != 0:
    for p in range(dados['partidas']):
        listagols.append(int(input(f'Quantos gols na partida {p+1}: ')))

dados['gols'] = listagols

dados['total'] = sum(listagols)        
print('-=-'*20)
print(dados)
print('-=-'*20)
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')

for v,l in enumerate(listagols):
    print(f'    =>Na partida {v+1}, fez {l}')
print(f'Foi um total de {sum(listagols)}')