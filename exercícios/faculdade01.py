#Lista de Exercícios – Variáveis, Expressões e Operadores Matemáticos

#1 Calcule o valor de cada expressão abaixo e indique o tipo do resultado (inteiro ou real)
import math
a = float(20 - 10)/2

b = 20 - 15/2

c = 2 * 5 / 20 + 30 / 15 * 2

d = 2*(5/20)+30/(15*2)

e = 23 / 4

f = 25%4

g = 35/6+2

h = 35/6-2

i = 35/6*2

j = math.sqrt(625)

k = math.pow(10,2)

l = 2+ math.sqrt(21/5)

print(f'Letra A: {a:.2f}')
print(f'Letra B: {b:.2f}')
print(f'Letra C: {c:.2f}')
print(f'Letra D: {d:.2f}')
print(f'Letra E: {e:.2f}')
print(f'Letra F: {f:.2f}')
print(f'Letra G: {g:.2f}')
print(f'Letra H: {h:.2f}')
print(f'Letra I: {i:.2f}')
print(f'Letra J: {j:.2f}')
print(f'Letra K: {k:.2f}')
print(f'Letra L: {l:.2f}')


#2 Escreva em Python, as seguintes expressões matemáticas:
a2 = (a+b)*c
b2 = (a+b+c+d+e+f+g+h+i+j+k+l) / 12
c2 = (a-b)+(c+d) /e
d2 = 'base**expoente'
e2 = (a*b)**c
f2 = math.sqrt(8+8)
print('2 questao:')
print(f'Letra A: {a2:.2f}')
print(f'Letra B: {b2:.2f}')
print(f'Letra C: {c2:.2f}')
print(f'Letra D: {d2}')
print(f'Letra E: {e2:.2f}')
print(f'Letra F: {f2:.2f}')


# Terceira Questao:
print('Terceira questao: ')


a_values = [3, 5, 2.5]
b_values = [16, 64, 9]
nome_values = ["MIRIAM", "PEDRO", "ANA"]
profissao_values = ["ADVOGADO", "MEDICO", "PROFESSOR"]
teste = False

# Função para avaliar as expressões
for i in range(3):
    a = a_values[i]
    b = b_values[i]
    nome = nome_values[i]
    profissao = profissao_values[i]

    # Expressão a
    expr_a = ((a + 1 >= math.sqrt(b)) or (not "Ana" == nome))

    # Expressão b
    expr_b = ((a + 1 >= math.sqrt(b)) and (profissao == "MEDICO"))

    # Expressão c
    expr_c = (not ("ANA" == nome)) or ((profissao == "Medico") and (a + 1 >= math.sqrt(b)))

    # Expressão d
    expr_d = (not teste) and ((a + 1 >= math.pow(b, 1))) or (not (profissao == "MEDICO"))

    # Expressão e
    expr_e = not ((a + 1 >= math.sqrt(b)) and teste)

    # Exibindo os resultados
    print(f"Linha {i + 1}:")
    print(f"a) {expr_a}")
    print(f"b) {expr_b}")
    print(f"c) {expr_c}")
    print(f"d) {expr_d}")
    print(f"e) {expr_e}")
    print()
    print("-" * 40)


   # Quarta questao:
#x = 0.0

#nome = ""

#cor = ""

#cod = False

#teste = False

#tudo = False


#(v) teste = cod or ((x)*2 != soma)

#(f) tudo = soma

#(f) x = nome >= cor

#(v) cod = cor = “verde”

#(f) tudo = !teste or cod and (soma < x)

#(v) nome = nome + cor



    # Quinta questao:
#Assinalar os comandos de atribuição inválidos, corrigindo-os quando possível:


i=0 #Valido

x, y, mult = 1, 2, 0 #Valido

flag = False #Valido

s = None #Valido

nome = '' #Valido

#sexo, opcao = 'f' /// #Invalido! // Forma certa:
sexo = 'f'
opcao = 'f'

mult = x * y #Valido

sexo = 'F' #Valido

i = x + y * 100 #Valido

i += 1 #Valido

nome = "12345" #Valido

opcao = "N" #Valido

flag = True #Valido

nome = "false" 
