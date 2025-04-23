class cliente:
    def __init__(self, nome, email, idade=0):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def exibir(self):
        print(self.nome, self.email, self.idade)
    

thiago = cliente('Thiago', 'britoff02@gmail.com', '17')

thiago.exibir()