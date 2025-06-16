# dataclasses

from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    _idade: int = field(default=0, repr=False)

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