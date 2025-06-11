
from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self):
        self._nome = None


    @property
    @abstractmethod
    def nome(self):
        ...
   
    
    @abstractmethod
    def atacar(self):
        ...
    
    @abstractmethod
    def defesa(self):
        ...
    
    @abstractmethod
    def habilidades(self):
        ...

class Guerreiro(Personagem):
    def __init__(self, nome=None):
        super().__init__()
        self._nome = nome
        
    
    @property
    def nome(self):
        return self._nome
    
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    def atacar(self):
        print(f'{self.nome} ESTA ATACANDO (GUERREIRO)')

    def defesa(self):
        print(f'{self.nome} ESTA DEFENDENDO (GUERREIRO)')
    
    def habilidades(self):
        print(f'{self.nome} (GUERREIRO)\n1-SOCO\n2-CHUTE')

    

p1 = Guerreiro('jose')
p1.atacar()
p1.defesa()
p1.habilidades()
p2 = Guerreiro()
p2.nome = 'Thiago'
p2.atacar()