times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'Sao Paulo', 'Corinthians', 'Bahia', 'Vasco da Gama')
print('Os 5 primeiros colocados: ')
print(f'{times[:5]}')
print('Os ultimos 4 colocados: ')
print(f'{times[-4:]}')
print(f'Em ordem alfabetica: ')
print(sorted(times))
print(f'O coritians esta na posicao : {times.index('Corinthians')}')