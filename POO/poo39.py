def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} - {class_dict}'
        return class_repr


def adiciona_repr(class_):
    class_.__repr__ = meu_repr
    return class_

def meu_planeta(metodo):
    def interno(self, *agrs, **kwargs):
        metodo = self.falar_nome()
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
        
    @meu_planeta
    def falar_nome(self):
         return f'O planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugual')
terra = Planeta('Terra')
marte = Planeta('Marte')
print(portugal)
print(brasil)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())