from abc import ABC, abstractmethod
from contas import ContaCorrente, ContaPoupanca

class Pessoa(ABC):
    def __init__(self):
        self._nome = None
        self._idade = None
        self._conta = None

    
    @property
    @abstractmethod
    def nome(self):
        ...
    
    @nome.setter
    @abstractmethod
    def nome(self):
        ...

    @property
    @abstractmethod
    def idade(self):
        ...
   
    @idade.setter
    @abstractmethod
    def idade(self):
        ...
    @property
    @abstractmethod
    def conta(self):
        ...
   
    @conta.setter
    @abstractmethod
    def conta(self):
        ...


class Cliente(Pessoa):
    def __init__(self, nome=None, idade=None, conta=None):
        self._nome = nome
        self._idade = idade
        self._conta = conta

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nome):
        self._idade = nome

    @property
    def conta(self):
        return self._conta
   
    @conta.setter
    def conta(self, conta):
        self._conta = conta


    def exibir(self):
        print(f'Cliente: {self._nome}, Idade:{self._idade}\n{self._conta}')
    
    def __repr__(self):
        return f'Cliente: {self._nome}, Idade:{self._idade}'

if __name__ == '__main__':
    conta_p1 = ContaCorrente('ITAU', 1234, 1000)
    p1 = Cliente('Thiago', 18, conta_p1)
    p1.exibir()

    conta_p2 = ContaPoupanca('NUBANK', 9999, 897.9)
    p2 = Cliente()
    p2.nome = 'Jose'
    p2.idade = 32
    p2.conta = conta_p2

    p2.exibir()
        