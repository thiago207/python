# Metodos em instancias de classes Python
class Carro:
    def __init__(self, nome='Sei la'):
        self.nome = nome

    def acelerar(self):
       print(f'{self.nome} esta acelerando...')
    
fusca = Carro(nome='Fusca')
print(fusca.nome)
Carro.acelerar(fusca)
#fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
Carro.acelerar(celta)
#celta.acelerar()