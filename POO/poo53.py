# dataclasses

from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    
    def __post_init__(self):     #DEPOIS DE INICIAR O PROGAMA CRIAS ESSE ATRIBUTO SEM PEDIR ELE OBRIGATORIAMENTE
        self.idade = None
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    p1 = Pessoa('thiago', 'felipe')
    p1.idade = 17
    print(p1)
    print(f'Idade: {p1.idade}')
    print(p1.nome_completo())