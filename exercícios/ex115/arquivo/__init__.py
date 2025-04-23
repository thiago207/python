def arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')