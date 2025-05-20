def adiciona(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona('luiz')
adiciona('Jose', cliente1)
print(cliente1)

cliente2 = adiciona('lipe')
adiciona('thiago', cliente2)
print(cliente2)