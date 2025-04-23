import os
from biblioteca import funcoes
def arquivo(nome):
    try:
        with open(nome, 'rt'):
            return True
    except FileNotFoundError:
        return False
    else:
        return True



def criar(nome):
    pasta = os.path.dirname(nome)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)  
    try:
        with open(nome, 'wt+') as a:
            print(f'Arquivo "{nome}" criado com sucesso!')
    except Exception as e:
        print(f'Houve um erro na criação do arquivo: {e}')

def leraquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Eroo ao ler o arquivo!')
    else:
        funcoes.linhas('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n','')
            print(f'{dados[0]:<30} {dados[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido',idade=0):
    try:
        a=open(arq, 'at')

    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()