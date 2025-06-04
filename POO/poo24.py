# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valorA'

    def __init__(self, nome):
        self.nome = nome

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valorB'

    def __init__(self, nome, valor):
        super().__init__(nome)
        self.valor = valor

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valorC'

    def metodo(self):
        #super().metodo() # PEGA O METODO DE B
        #super(B, self).metodo() # PEGA O METODO DE A
        #super(A, self).metodo() # PEGA O METODO DE OBJ
        print('C')


c = C('Thiago','Futuro Estagiario')

#print(c.atributo_a, c.atributo_b, c.atributo_c)

print(c.nome, c.valor)

