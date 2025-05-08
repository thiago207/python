from math import sqrt

def menu():
    historico = []
    print("=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("7 - Ver histórico")
    print("0 - Sair")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                print("Encerrando a calculadora...")
                break
            
            if opcao == 7:
                if historico:
                    for e,v in enumerate(historico):
                        print(f'{e+1}) {v}')
                else:
                    print("Nenhum cálculo realizado ainda.")
                continue

                
                
            if opcao not in [1, 2, 3, 4, 5, 6,7]:
                print("Opção inválida.")
                continue


            if opcao == 6:
                try:
                    n = int(input('Qual numero deseja saber a raiz quadrada: '))
                    if n < 0:
                        print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
                        continue
                    resultado = sqrt(n)
                    calculo = f'√{n} = {resultado:.2f}'
                    historico.append(calculo)
                    print(calculo)

                except ValueError:
                    print('Erro: Entrada inválida. Digite um número válido.')
                continue
                    
            
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            if opcao == 1:
                resultado = n1 + n2
                calculo = f'{n1} + {n2} = {resultado}'
                historico.append(calculo)
                print(calculo)

            elif opcao == 2:
                resultado =  n1 - n2
                calculo = f'{n1} - {n2} = {resultado}'
                historico.append(calculo)
                print(calculo)

            elif opcao == 3:
                resultado = n1 * n2
                calculo = f'{n1} x {n2} = {resultado}'
                historico.append(calculo)
                print(calculo)

            elif opcao == 4:
                if n2 == 0:
                    print(f'ERRO DIVISAO POR (0)')
                    continue

                resultado = n1 / n2
                calculo = f'{n1} / {n2} = {resultado}'
                historico.append(calculo)
                print(calculo)

            elif opcao == 5:

                resultado = n1 ** n2
                calculo = f'{n1} ** {n2} = {resultado}'
                historico.append(calculo)
                print(calculo)

        except ValueError:
            print('DIGITE VALORES VALIDOS.')

menu()