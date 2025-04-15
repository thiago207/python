def ajuda(com):
    help(com)

def personalizacao(linhas, cor=0):
    print('-=-' *10)
    print(linhas)
    print('-=-' *10)



comando = ''
while True:
    
    comando = str(input('FUNCAO OU BIBLIOTECA > '))
    
    if comando.upper() =='FIM':
        break
    else:
        personalizacao(f'   ACESSANDO O MANUAL DO {comando}')
        ajuda(comando)
    personalizacao('    SISTEMA DE AJUDA PyHELP')
personalizacao('   FIM DO PROGRAMA')