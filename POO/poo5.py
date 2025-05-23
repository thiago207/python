#Mentendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja esta filmando')
            return
        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def para_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NAO esta filmando')
            return
        print(f'{self.nome} parando de filmar...')
        self.filmando = False

    def fotagrafar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotagrafar filmando')
            return
        print(f'{self.nome} esta fotagrafando!')
        self.foto = True


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()  
c1.filmar() 
c1.fotagrafar()
c1.para_de_filmar()
c1.fotagrafar()

