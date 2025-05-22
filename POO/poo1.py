# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome




p1 = Pessoa('Luiz', 'Otavio')
#p1.nome = 'Thiago'
#p1.sobrenome = 'Felipe'
print(p1.nome, p1.sobrenome)

p2 = Pessoa('Maria', 'Josefa')

print(p2.nome, p2.sobrenome)