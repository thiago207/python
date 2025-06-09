#Crie uma classe base Funcionario, e duas subclasses Engenheiro e Gestor,
#cada uma com um método trabalhar() específico. Depois, 
#crie uma classe EngenheiroGestor que herda de ambas e implemente o comportamento correto.

class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        self._trabalhando = False
    def trabalhar(self):
        if not self._trabalhando:
            self._trabalhando = True
            print(f'{self.nome} esta trabalhando')  

        else:
            print(f'{self.nome} ja esta trabalhando')
        return
    def parar_trabalhar(self):
       self._trabalhando =  False
       print(f'{self.nome} parou de trabalhar') 
       return 


    
class Engenheiro(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
    def trabalhar(self):
        super().trabalhar()
        print('ENGENHEIRO')


class Gestor(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
    def trabalhar(self):
        super().trabalhar()
        print('gestor')

class EngenheiroGestor(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def trabalhar(self):
        super().trabalhar()
        print('como : engenheiro/gestor')

p1 = EngenheiroGestor('thiago')
p1.trabalhar()

p1.parar_trabalhar()

p1.trabalhar()

p1.trabalhar()

p1.trabalhar()
