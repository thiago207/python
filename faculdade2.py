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
