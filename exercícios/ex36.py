casa = float(input('Qual valor da casa? '))
salario = float(input('Qual seu salario? '))
anos = float(input('Em quantos anos vai pagar? '))

prestacao = casa / (anos * 12)
exceder = salario * 30 / 100


print(f'Para pagar uma casa de R${casa:.2f} em {anos} a prestaçao sera de \n {prestacao:.2f}')
if prestacao <= exceder:
    print('Emprestimo pode ser feito')
else:
    print('Nao pode ser feito')



