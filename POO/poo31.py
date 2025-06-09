#Exercício 1 – Interface de Animal
#Crie uma classe abstrata Animal com os métodos:

#falar() (abstrato)

#mover() (abstrato)

#Depois, crie duas subclasses: Cachorro e Peixe, que implementam esses métodos com comportamentos diferentes.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        """Método abstrato que deve ser implementado pelas classes filhas"""
        ...
    @abstractmethod
    def mover(self):
        """Método abstrato que deve ser implementado pelas classes filhas"""
        ...

class Cachorro(Animal):
    def falar(self):
        print('AUAU')

    def mover(self):
        print('CACHORRO ESTA ANDANDO')
        
class Peixe(Animal):
    def falar(self):
        print('peixe nao fala kkkk')
    def mover(self):
        print('PEIXE ESTA NADANDO')
    
c = Cachorro()
p = Peixe()

p.falar()  # Output: peixe nao fala kkkk
c.falar()  # Output: AUAU
c.mover()  # Output: CACHORRO ESTA ANDANDO
p.mover()  # Output: PEIXE ESTA NADANDO


#Exercício 2 – Interface com @classmethod
#Crie uma classe abstrata Arquivo com:

#Um método abstrato @classmethod carregar(caminho) que deve ser implementado por subclasses.

#Uma subclasse ArquivoCSV que simula a leitura de um arquivo CSV e imprime "Carregando arquivo.csv".


class Arquivo(ABC):

    @classmethod
    @abstractmethod
    def carregar(cls, caminho):
        ...

class ArquivoCSV(Arquivo):
    @classmethod
    def carregar(cls, caminho):
        print(f"Carregando {caminho}")
        return cls()
    
ArquivoCSV.carregar("dados/vendas.csv")

#Exercício 3 – Produto com preço
#Crie uma classe abstrata Produto com:

#Um atributo preco que deve ser acessado via @property e @setter.

#A propriedade deve impedir valores negativos.

#Depois, crie a subclasse Livro que implementa isso e adicione um método descricao() que imprime nome e preço.

class Produto(ABC):
    def __init__(self):
        self._nome = None
        self._preco = 0.0
    
    @property
    @abstractmethod
    def nome(self):
        ...
    @nome.setter
    def nome(self, nome):
        ...
        
    @property
    @abstractmethod
    def preco(self):
        ...
    @preco.setter
    def preco(self, preco):
        ...

class Livro(Produto):
    def __init__(self, nome=None, preco=0.0):
        super().__init__()
        if nome:
            self._nome = nome
        if preco < 0:
            self._preco = 'ERRO'
        else:
            self._preco = preco

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        if nome.strip() == '':
            raise ValueError ('O nome nao pode ser vazio! ')
        self._nome = nome

    @property
    def  preco(self):
        return self._preco
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError('O preço não pode ser negativo!')
        self._preco = preco
    def descricao(self):
        print(f'Nome: {self._nome} \nPreço: {self._preco}')

l = Livro()
l.nome = 'NADA PODE ME FERIR'
l.preco = 29.90
l.descricao()
l2 = Livro("O Alquimista", 25.50)
l2.descricao()

#Exercício 5 – Sistema de autenticação
#Crie uma classe abstrata Usuario com:

#@property login (abstrato)

#@property senha (abstrato)

#Um método abstrato autenticar()

#Implemente a classe UsuarioEmail onde login é um e-mail. O método autenticar() deve verificar se a senha é "123456".

class Usuario(ABC):
    def __init__(self):
        self._login = None
        self._senha = None
    
    @property
    @abstractmethod
    def senha(self):
        ...
    @senha.setter
    @abstractmethod
    def senha(self, senha):
        ...
    @property
    @abstractmethod
    def login(self):
        ...
    @login.setter
    @abstractmethod
    def login(self, email):
        ...

class UsuarioEmail(Usuario):
    def __init__(self, login=None, senha=None):
        super().__init__()
        self._login = login
        self._senha = senha

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, email):
        self._login = email
    
    def autenticar(self):
        if self._senha == '123456':
            print('LOGIN VALIDO')
            return
        print(f'SENHA INVALIDA INVALIDA')
    
u = UsuarioEmail()
u.login = 'vouserfoda.@gmail.com'
u.senha = '123456'
print(u.login, u.senha)
u.autenticar()

