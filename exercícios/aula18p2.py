'''teste = []
teste.append('Lipe')
teste.append(17)
galera = []
teste[0] = 'Maria'
teste[1] = 90
galera.append(teste[:])
print(galera)'''
'''galera = [['Jorge',80], ['Ana', 20], ['Thiago', 17]]
n = 1
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade')'''
galera = []
dados = []
maior = menor = 0
for c in range (2):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    print(f'Temos {p[0]} com {p[1]}')
for i in galera:
    if i[1] >= 18:
        print(f'{i[0]} é maior')
        maior += 1
    else:
        menor += 1
        print(f'{i[0]} é menor')

print(f'E {maior} de idade e {menor}de idade')      