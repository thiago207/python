# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): 
        ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)



class Pagamento(ABC):
    @abstractmethod
    def pagar(self):
         ...
    @abstractmethod
    def receber(self):
         ...
class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f'Pago no valor de {valor}')
    
    def receber(self, valor):
        print(f'Recebido no valor de {valor}')
    
p1 = PagamentoPix()
p1.pagar(11)
p1.receber(1002)
    

