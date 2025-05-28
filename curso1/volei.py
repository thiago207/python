print('-=-' * 20)
print('Jogo VOLEI!')
print('-=-' * 20)
cont1 = cont2 = 0
a1 = a2 = 0
dados = {}
listanome = []
listanome.append(str(input('Nome equipe 1: ')))
listanome.append(str(input('Nome equipe 2: ')))
dados['nome'] = listanome

print(f'{listanome[0]} X {listanome[1]}')

while True:
    print('-' * 20)
    while True:
        pontos = int((input('Quem fez os pontos? [ 1 / 2 ]  ')))
        if pontos == 1:
            break
        if pontos == 2:
            break
        else:
            print('Opcao invalida!')
    if pontos == 1:
        cont1 +=1
    if pontos == 2:
        cont2 +=1
    print('-' * 20)
    print(f'-{listanome[0]}  X  {listanome[1]}')
    print(f'{cont1}  {listanome[0]} -- {cont2}  {listanome[1]}')

    if cont1 == 5:
        break
    if cont2 == 5:
        break
if cont1 > cont2:
    print(f'O time {listanome[0]} venceu!!')
    print(f'DE {cont1} a {cont2}')
else:
    print(f'O time {listanome[0]} venceu!!')
    print(f'DE {cont1} a {cont2}')



