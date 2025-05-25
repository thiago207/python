# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def anonimo(cls, idade):
        return cls('Anonima', idade)
    
    
p1 = Pessoa('Jao', 43)
Pessoa.metodo_de_classe()
p2 = (Pessoa.criar_com_50_anos('jose'))
p3 = Pessoa.anonimo(76)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
