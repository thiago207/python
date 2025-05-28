class Produto:
    def __init__(self, nome, preco=None):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self._preco = novo_preco
            return
        raise ValueError('Preço invalido!!')
    
    @classmethod
    def criar_com_desconto(cls, nome, preco_original, percentual_desconto):
        novo_preco = preco_original - (preco_original * percentual_desconto / 100)
        return cls(nome, novo_preco)

    def exibir(self):
        print(
              f'Produto: {self.nome}\nPreço: {self.preco:.2f}'
        )
        print()


p1 = Produto('Notebook')
p1.preco = 3299
p1.exibir()

p2 = Produto.criar_com_desconto('Celular', 2000, 20)
p2.exibir()