# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, valor):
        if isinstance(valor, (int,float)):
            raise ValueError('TEM QUE SER STRING!')
        
        self._cor = valor
        return
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

c1 = Caneta('blue') 

c1.cor = 'rosa'# setter -> cria valor
c1.cor_tampa = 'preta'# setter -> cria valor

print(c1.cor_tampa)

print(c1.cor) # getter -> obter valor

