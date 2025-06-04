class Animal:
    def __init__(self, nome):
        self. nome = nome
    
    def som(self):
        print('O animal fez um som')
    def acao(self):
        print('O animal fez uma açao')
class Dog(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    
    def som(self):
        super().som()
        print(f'O {self.nome} latiu...')
    
    def andar(self):
        super().acao()
        print(f'O {self.nome} andou')
    
dog1 = Dog('Zeus', 'Ratinho')
dog1.som()
dog1.andar()