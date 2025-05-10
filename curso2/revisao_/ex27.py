
# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

'''def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)'''
def criar_funcao(func):

    def interna(*args):
        lista = []
        for agr in args:
            agrs_convertidos = e_string(agr)
            lista.append(agrs_convertidos)
        resultado = func(*lista)
        return resultado
    return interna


@criar_funcao
def inverte(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        return str(param)
    return param
        
    

invertida = inverte(123)
print(invertida)