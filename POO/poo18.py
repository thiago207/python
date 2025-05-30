# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        for p in produtos:
            self._produtos.append(p)

    def listar_produtos(self):
        print()
        for p in self._produtos:
            print(p.nome, p.preco)
        print()
        
    def aumentar_10reais(self, *produtos):
        for p in produtos:
            p.preco += 10

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carinho()
p1, p2 = Produto('Nootebook', 3299), Produto('Celular', 2500)
carrinho.inserir_produtos(p1, p2)
carrinho.aumentar_10reais(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())