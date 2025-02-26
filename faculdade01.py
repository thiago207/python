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


# Definindo as variáveis
teste = False

# Dados das linhas
variaveis = [
    {'a': 3, 'b': 16, 'nome': "MIRIAM", 'profissao': "ADVOGADO"},
    {'a': 5, 'b': 64, 'nome': "PEDRO", 'profissao': "MEDICO"},
    {'a': 2.5, 'b': 9, 'nome' : "ANA", 'profissao': "PROFESSOR"}
]

# Função para avaliar as expressões
def avaliar_expressao(variaveis, teste):
    resultados = []

    for var in variaveis:
        a = var['a']
        b = var['b']
        nome = var['nome']
        profissao = var['profissao']

        # Expressão (a)
        resultado_a = (a + 1 >= math.sqrt(b)) or (not "Ana" == nome)

        # Expressão (b)
        resultado_b = (a + 1 >= math.sqrt(b)) and (profissao == "MEDICO")

        # Expressão (c)
        resultado_c = (not "ANA" == nome) or (profissao == "Medico" and a + 1 >= math.sqrt(b))

        # Expressão (d)
        resultado_d = not teste and ((a + 1) >= math.pow(b, 1)) or not (profissao == "MEDICO")

        # Expressão (e)
        resultado_e = not ((a + 1 >= math.sqrt(b)) and teste)

        # Armazenando os resultados
        resultados.append({
            'linha': var,
            'resultado_a': resultado_a,
            'resultado_b': resultado_b,
            'resultado_c': resultado_c,
            'resultado_d': resultado_d,
            'resultado_e': resultado_e
        })

    return resultados

# Avaliando as expressões
resultados = avaliar_expressao(variaveis, teste)

# Exibindo os resultados
for resultado in resultados:
    print(f"Para a linha {resultado['linha']}:")
    print(f"  (a) {resultado['resultado_a']}")
    print(f"  (b) {resultado['resultado_b']}")
    print(f"  (c) {resultado['resultado_c']}")
    print(f"  (d) {resultado['resultado_d']}")
    print(f"  (e) {resultado['resultado_e']}")
    print("-" * 40)
