from random import randint
from operator import itemgetter
jogadas = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)
}
ranking = dict()
for k,v in jogadas.items():
    print(f'O {k} tirou {v}')


ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')



        
    
    