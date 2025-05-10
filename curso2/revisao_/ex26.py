#Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def contatenar(string_inicial=''):
    valor_final = string_inicial
    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = contatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

#def multiplicador(valor):
#    def mutiplicado(valor_b):
#        valor_final = valor * valor_b
#        return valor_final
#    return mutiplicado
#valor = multiplicador(2)
#v1 = valor(10)
#print(v1)

