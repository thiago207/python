print('-'*20)
print("LISTAGEM DE PREÇOS")
print('-'*20)
produtos = ('Lapis',1.75,
            'Caderno', 2.00,
            'Livro', 35.5,
            'Canetas',22.00,
            'Estojo',25.00)
for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R$ {produtos[pos]}')