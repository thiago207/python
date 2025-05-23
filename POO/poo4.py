#Crie uma classe Aluno com atributos como nome, matrícula e notas. Adicione métodos para calcular a média e exibir o status (aprovado/reprovado).

class Aluno:
    def __init__(self, nome, matricula, *notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    def media(self):
        v = list(self.notas)
        media = sum(v) / len(v)
        print()
        if media >= 7:
            print(f'{self.notas}\nAPROVADO COM {media}') 
            return
        print(f'{v}\nREPROVADO COM {media:.1f}') 



aluno1 = Aluno('Thiago', '000576342', 8 , 6.5 , 6.5)
print(aluno1.nome)
print(aluno1.matricula)
print(aluno1.notas)
aluno1.media()

