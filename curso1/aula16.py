lanche = ('Hambueguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas sao imutáveis
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi bastante!!!')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na    posicao {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
