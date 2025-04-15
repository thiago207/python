def ajuda(com):
    help(com)




comando = ''
while True:
    comando = str(input('FUNCAO OU BIBLIOTECA > '))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
