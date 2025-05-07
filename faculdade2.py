# 1 questao>
soma_imposto = 0

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


print(f'O total de imposto que a empresa deve pagar é de: R$: {soma_imposto:.2f}')

# 2 questao>

for c in range(50, 251):
    print(f'{c} o quadrado desse numero é {c**2}')
    print()

# 3 questao> 
cont = 0
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
print(f'A media desses salarios foi de {media_salario}')

# 4 questao>
cont = 0
soma_medias_alunos = 0

n = int(input('Quantos alunos tem nessa turma? '))

if n > 0:
    for a in range(n):
        nota_alunos = float(input(f'Qual a nota do {a+1}º aluno: '))
        

        soma_medias_alunos += nota_alunos
        
else:
    print('VALOR INVALIDO.')
    
media_notas = soma_medias_alunos / n
print(f'A media dos alunos foi: {media_notas}')

# 5 questao> 
numero = int(input('Qual numero deseja saber o fatorial? '))
fatorial = 1
cont=0
sequencia = 0
if numero > 0:
    for n in range(1,numero+1):
        fatorial *= n

else:
    print(f'DIGITE UM VALOR VALIDO')

print(f'SEU NUMERO {numero} fatorado é igual a {fatorial}')

# 6 questao >


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


homens_peso_acima_90_idade_50 = ''
mulheres_menor_idade = ''

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
            homens_peso_acima_90_idade_50 = nome

    if sexo == 'F':
        if idade < 18:
            mulheres_menor_idade = nome


media_altura_homens = soma_altura / cont_a
media_pesos_mulheres = soma_peso_mulher / cont_p


print(f'A media de altura dos homens foi de: {media_altura_homens:.1f}')
print()
print(f'A media dos pesos das mulheres foi de: {media_pesos_mulheres:.1f}')
print()
print(f'O homem mais alto foi {nome_homem_mais_alto} com {homem_mais_alto}')
print()
print('Nome dos homens com peso maior do que 90 e idade maior do que 50: {homens_peso_acima_90_idade_50}')


print('Nome das mulheres menores de idade: {mulheres_menor_idade}')



#8 questao> 

intervalo1 = 0  # [0, 25]
intervalo2 = 0  # (25, 50]
intervalo3 = 0  # (50, 75]
intervalo4 = 0  # (75, 100]

print("Digite os valores (número negativo para encerrar):")

while True:
    valor = float(input("Valor: "))

    if valor < 0:
        break  

    if 0 <= valor <= 25:
        intervalo1 += 1
    elif 25 < valor <= 50:
        intervalo2 += 1
    elif 50 < valor <= 75:
        intervalo3 += 1
    elif 75 < valor <= 100:
        intervalo4 += 1
    else:
        print("Valor fora do intervalo [0,100] — ignorado.")


print("\nContagem por intervalos:")
print(f"[0,25]     : {intervalo1}")
print(f"(25,50]    : {intervalo2}")
print(f"(50,75]    : {intervalo3}")
print(f"(75,100]   : {intervalo4}")


#9 questao> 

a = 1
b = 1
soma = a + b  

print("100 primeiros termos da série de Fibonacci:")
print(a)
print(b)


for i in range(3, 101):
    termo = a + b
    print(termo)
    soma += termo
    a = b
    b = termo


print(f"\nSoma dos 100 primeiros termos: {soma}")


#10 questao>

nascimentos = int(input("Digite o número total de crianças nascidas no período: "))

total_mortes = 0
mortes_femininas = 0
mortes_ate_24_meses = 0

while True:
    sexo = input("Digite o sexo da criança morta (masculino/feminino) ou 'vazio' para encerrar: ").strip().lower()
    
    if sexo == "vazio":
        break

    meses = int(input("Digite o número de meses de vida da criança: "))
    total_mortes += 1

    if sexo == "feminino":
        mortes_femininas += 1

    if meses <= 24:
        mortes_ate_24_meses += 1


if nascimentos > 0:
    perc_mortalidade_geral = (total_mortes / nascimentos) * 100
    perc_mortalidade_feminina = (mortes_femininas / nascimentos) * 100
    perc_mortes_ate_24 = (mortes_ate_24_meses / nascimentos) * 100

    print(f"\nRelatório da mortalidade infantil:")
    print(f"Percentual de crianças mortas: {perc_mortalidade_geral:.2f}%")
    print(f"Percentual de meninas mortas: {perc_mortalidade_feminina:.2f}%")
    print(f"Percentual de crianças que viveram 24 meses ou menos: {perc_mortes_ate_24:.2f}%")
else:
    print("Número de nascimentos deve ser maior que zero.")


#11 questao >
aud_cultura = 0
aud_sbt = 0
aud_globo = 0
aud_record = 0
aud_mtv = 0
total_pessoas = 0

print("Pesquisa de audiência de TV")
print("Digite o canal assistido ou 'fim' para encerrar.")
print("Canais disponíveis: Cultura, SBT, Globo, Record, MTV")

while True:
    canal = input("\nCanal: ").strip().lower()
    
    if canal == "fim":
        break

    pessoas = int(input("Número de pessoas assistindo: "))
    
    if canal == "cultura":
        aud_cultura += pessoas
    elif canal == "sbt":
        aud_sbt += pessoas
    elif canal == "globo":
        aud_globo += pessoas
    elif canal == "record":
        aud_record += pessoas
    elif canal == "mtv":
        aud_mtv += pessoas
    else:
        print("Canal inválido. Dados ignorados.")
        continue  # não soma ao total

    total_pessoas += pessoas


if total_pessoas > 0:
    perc_cultura = (aud_cultura / total_pessoas) * 100
    perc_sbt = (aud_sbt / total_pessoas) * 100
    perc_globo = (aud_globo / total_pessoas) * 100
    perc_record = (aud_record / total_pessoas) * 100
    perc_mtv = (aud_mtv / total_pessoas) * 100

    print("\nPercentual de audiência por canal:")
    print(f"Cultura: {perc_cultura:.2f}%")
    print(f"SBT:     {perc_sbt:.2f}%")
    print(f"Globo:   {perc_globo:.2f}%")
    print(f"Record:  {perc_record:.2f}%")
    print(f"MTV:     {perc_mtv:.2f}%")

    
    maior_aud = aud_cultura
    menor_aud = aud_cultura
    canal_maior = "Cultura"
    canal_menor = "Cultura"

    if aud_sbt > maior_aud:
        maior_aud = aud_sbt
        canal_maior = "SBT"
    elif aud_sbt < menor_aud:
        menor_aud = aud_sbt
        canal_menor = "SBT"

    if aud_globo > maior_aud:
        maior_aud = aud_globo
        canal_maior = "Globo"
    elif aud_globo < menor_aud:
        menor_aud = aud_globo
        canal_menor = "Globo"

    if aud_record > maior_aud:
        maior_aud = aud_record
        canal_maior = "Record"
    elif aud_record < menor_aud:
        menor_aud = aud_record
        canal_menor = "Record"

    if aud_mtv > maior_aud:
        maior_aud = aud_mtv
        canal_maior = "MTV"
    elif aud_mtv < menor_aud:
        menor_aud = aud_mtv
        canal_menor = "MTV"

    print(f"\nMaior audiência: {canal_maior} ({maior_aud} pessoas)")
    print(f"Menor audiência: {canal_menor} ({menor_aud} pessoas)")

else:
    print("\nNenhuma casa registrada com TV ligada.")
