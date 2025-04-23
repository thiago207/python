from dataclasses import dataclass

@dataclass
class cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(
            f'Meu nome é {self.nome}, tenho {self. idade} anos e meu e-mail é: {self.email}'
        )

thiago = cliente('thiago', 'britoff02@GMAIL.COM', 17)

thiago.exibir()