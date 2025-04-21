from biblioteca import funcoes
funcoes.linhas('115A')
from time import sleep
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
