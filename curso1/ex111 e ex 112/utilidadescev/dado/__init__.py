'''def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO : {entrada} é um preço invalido! ')
        else:
            valido = True
            return float(entrada)'''
def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input('Digite seu preço: ')).strip().replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: {entrada} NAO É VALIDA!')
        else:
            valido = True
            return float(entrada)
