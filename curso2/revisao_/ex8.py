def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

lista = ['Thiago', 'Fred', 'Luiz']

for nome in lista:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))