somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----{p} PESSOA-----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/f]:')).strip()
    somaidade += idade
    mediaidade = somaidade / 4

    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


    

    

print(f'A media de idade foi {mediaidade}')
print(f'O homem mais velho tem {maioridadedehomem} e se chama {nomevelho.title()}')
print(f'Ao todo sao {totmulher20} com menos de 20 anos ')

