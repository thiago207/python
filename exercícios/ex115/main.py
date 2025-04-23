from biblioteca import funcoes
from arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivo(arq):
    criar(arq)



while True:

    resposta = funcoes.menu(['Ver pessoas cadrastradas' , 'Cadastrar nova pessoa' , 'Sair do progama'])

    if resposta == 1:
        funcoes.linhas('op 1')
    elif resposta == 2:
        funcoes.linhas('op 2')
    elif resposta == 3:
        funcoes.linhas('Ate logo..')
        break
    else:
        print('Digite uma opcao valida')
    sleep(1)
