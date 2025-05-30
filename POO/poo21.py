class Motor:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros_fabricados = []

    def __str__(self):
        return self.nome
    
    def adicionar_carro(self, carro):
        self._carros_fabricados.append(carro)

    def listar_carros_fabricados(self):
        print(f'Carros fabricados por {self.nome}:')
        for carro in self._carros_fabricados:
            print(f'- {carro.nome} (Motor: {carro.motor})')

class Carro: 
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
        fabricante.adicionar_carro(self)

    def __str__(self):
        return f'{self.nome} - Motor: {self.motor} - Fabricante: {self.fabricante}'

motor1 = Motor('V8')
motor2 = Motor('1.0 Turbo')

fabricante1 = Fabricante('Toyota')
fabricante2 = Fabricante('Ford')

carro1 = Carro('BMW', motor2, fabricante1)
print(carro1)
carro2 = Carro('AUDI', motor1, fabricante2)
print(carro2)

fabricante2.listar_carros_fabricados()