def recusivo(inicio=0,fim=10):
    if inicio >= fim:
        return fim
    print(inicio,fim)
    inicio += 1
    return recusivo(inicio, fim)
print(recusivo())