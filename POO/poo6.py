# Atributos de classe
from datetime import date

class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def ano_nascimento(self):
        if isinstance(self.idade, str):
            self.idade = int(self.idade)

        return f'{self.nome} < nasceu em > {Pessoa.ano_atual - self.idade}'

p1 = Pessoa('thiago', '18')
print(Pessoa.ano_atual)
print(p1.ano_nascimento())