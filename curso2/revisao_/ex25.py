'''def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def arg(y):
        return funcao(x,y)
    return arg


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(10))

multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(10))'''



def divide(x,y):
    
    return x / y
        

def criar_funcao(funcao,x):
    def segundo_elemento(y):
        try:
            return funcao(y,x)
        except:
            print('ZeroDivisionError')
    return segundo_elemento

divide_por_dois = criar_funcao(divide, 2)
print(divide_por_dois(8))
