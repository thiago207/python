from biblioteca import funcoes
from arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivo(arq):
    criar(arq)



while True:

    resposta = funcoes.menu(['Ver pessoas cadrastradas' , 'Cadastrar nova pessoa' , 'Sair do progama'])

    if resposta == 1:
        leraquivo(arq)
    elif resposta == 2:
        funcoes.linhas('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = funcoes.leiaint('IDADE: ')
        cadastrar(arq, nome , idade)
    elif resposta == 3:
        funcoes.linhas('Ate logo..')
        break
    else:
        print('Digite uma opcao valida')
    sleep(1)
