class Pessoa():
    ano_atual = 2025
    def __init__(self, nome, idade=None):
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, nova_idade):
        if 0 < nova_idade < 120:
            self._idade = nova_idade
        else:
            raise ValueError('IDADE IMPOSSIVEL')
    @classmethod
    def criar_com_ano_de_nascimento(cls, nome, data_nascimento):
        data_nascimento = 2025 - data_nascimento 
        return cls(nome, data_nascimento)



p1 = Pessoa('Thiago')
print(p1.nome)        
p1.idade = 100
print(p1.idade)    
p2 = Pessoa.criar_com_ano_de_nascimento('Juliana', 2005)
print(p2.nome)
print(p2.idade)