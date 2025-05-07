# 1 questao>
'''soma_imposto = 0

for imposto in range (501):
    valor = float(input('Digite seu valor base: '))

    if 1600 < valor <=3000:
        calculo_imposto = valor * 10 / 100
        soma_imposto += calculo_imposto
        print(f'O imposto para esse valor é {calculo_imposto}')
        print()

    elif 3000 < valor <= 7000:
        calculo_imposto = valor * 15 / 100
        soma_imposto += calculo_imposto
        print(f'O imposto para esse valor é {calculo_imposto}')
        print()

    elif valor > 7000:
        calculo_imposto = valor * 20 /100
        soma_imposto += calculo_imposto
        print(f'O imposto para esse valor é {calculo_imposto}')
        print()

    else:
        print('ISENTO DE IMPOSTO')
print()


print(f'O total de imposto que a empresa deve pagar é de: R$: {soma_imposto:.2f}')'''

# 2 questao>

'''for c in range(50, 251):
    print(f'{c} o quadrado desse numero é {c**2}')
    print()'''

# 3 questao> 
'''cont = 0
soma_salarios = 0
while True:
    salario = float(input('Qual valor do salario?[-1 para encerar o progama] '))
    if salario > 0:
        cont +=1
        soma_salarios += salario
        print('Salario salvo no progama.')
    else:
        break

media_salario = soma_salarios / cont
print(f'A media desses salarios foi de {media_salario}')'''

# 4 questa>
'''cont = 0
soma_medias_alunos = 0

n = int(input('Quantos alunos tem nessa turma? '))

if n > 0:
    for a in range(n):
        nota_alunos = float(input(f'Qual a nota do {a+1}º aluno: '))
        

        soma_medias_alunos += nota_alunos
        
else:
    print('VALOR INVALIDO.')
    
media_notas = soma_medias_alunos / n
print(f'A media dos alunos foi: {media_notas}')'''

# 5 questao> 
'''numero = int(input('Qual numero deseja saber o fatorial? '))
fatorial = 1
cont=0
sequencia = 0
if numero > 0:
    for n in range(1,numero+1):
        fatorial *= n

else:
    print(f'DIGITE UM VALOR VALIDO')

print(f'SEU NUMERO {numero} fatorado é igual a {fatorial}')'''

# 6 questao >

'''
mais_alta = 0
segunda_mais_alta = 0

for i in range(1, 201):
    altura = float(input(f"Digite a altura da candidata {i}: "))

    if altura > mais_alta:
        segunda_mais_alta = mais_alta
        mais_alta = altura
    elif altura > segunda_mais_alta:
        segunda_mais_alta = altura


print(f"A candidata mais alta tem {mais_alta:.2f} metros.")
print(f"A segunda candidata mais alta tem {segunda_mais_alta:.2f} metros.")
'''

# 7 questao >
ler = 0

cont_a = 0
soma_altura = 0
media_altura_homens = 0

cont_p = 0
soma_peso_mulher = 0
media_pesos_mulheres = 0

homem_mais_alto = 0
nome_homem_mais_alto = ''

mulher_mais_gorda = 0
nome_mulher_mais_gorda = ''


homens_peso_acima_90_idade_50 = []
mulheres_menor_idade = []

while ler != 2:
    ler += 1
    nome = str(input('Digite seu nome: '))
    sexo = input("Sexo (M/F): ").strip().upper()
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    if sexo == 'M':
        cont_a += 1
        soma_altura += altura

    if sexo == 'F':
        cont_p += 1
        soma_peso_mulher += peso

    if sexo == 'M':
        if altura > homem_mais_alto:
            nome_homem_mais_alto = nome
            homem_mais_alto = altura
    if sexo == 'F':
        if peso > mulher_mais_gorda:
            nome_mulher_mais_gorda = nome
            mulher_mais_gorda = peso

    if sexo == 'M':
        if peso > 90 and idade > 50:
            homens_peso_acima_90_idade_50.append(nome)

    if sexo == 'F':
        if idade < 18:
            mulheres_menor_idade.append(nome)


media_altura_homens = soma_altura / cont_a
media_pesos_mulheres = soma_peso_mulher / cont_p


print(f'A media de altura dos homens foi de: {media_altura_homens:.1f}')
print()
print(f'A media dos pesos das mulheres foi de: {media_pesos_mulheres:.1f}')
print()
print(f'O homem mais alto foi {nome_homem_mais_alto} com {homem_mais_alto}')
print()
print('Nome dos homens com peso maior do que 90 e idade maior do que 50: ')
for nome in homens_peso_acima_90_idade_50:
    print(' -', nome)

print('Nome das mulheres menores de idade: ')
for nome in mulheres_menor_idade:
    print(' -', nome)
