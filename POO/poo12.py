# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

'''class Caneta:
    def __init__(self, cor=None):
        self.cor = cor


    def get_cor(self):
        return self.cor
    

c1 = Caneta('blue') 
print(c1.get_cor())'''

class Caneta:
    def __init__(self, cor,cor_da_tampa):
        self.cor_nome_diferente = cor
        self.cor_da_tampa = cor_da_tampa
    @property
    def cor(self):
        return self.cor_nome_diferente

    @property
    def cor_tampa(self):
        return self.cor_da_tampa
c1 = Caneta('blue','vermelho') 
print(c1.cor)
print(c1.cor_nome_diferente)
print(c1.cor_tampa)