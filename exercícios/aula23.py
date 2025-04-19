while True:
    try:
        n1 = int(input('N1: '))
        n2 = int(input('N1: '))
        r = n1 / n2
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que voce digitou.')
        valor = False
    except ZeroDivisionError:
        print('Nao foi possivel dividir o numero por zero')
        valor = False
    except KeyboardInterrupt:
        print('O usuario preferio nao informar os dados!')
        valor = False
    except Exception as erro:
        print(F'ERRO! O ERRO FOI {erro.__class__}')
        valor = False
    else: 
        print(r)
        valor = True
    finally:
        print('VOLTE SEMPRE!')
    if valor:
        break