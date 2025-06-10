# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...
    
class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print(f'Email: enviando - {self.mensagem}')
        return True

class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print(f'SMS: enviando - {self.mensagem}')
        return True
    
#n = NotificacaoEmail('Bom dia')
#n.enviar()

def notificar(noticacao: Notificacao):
    notificacao_enviada = noticacao.enviar()
    
    if notificacao_enviada:
        print('Notificaçao enviada')
    else:
        print('Notificaçao NAO enviada')
        
    
noti_email = NotificacaoEmail('TESTE EMAIL')
notificar(noti_email)

noti_sms = NotificacaoSMS('TESTE EMAIL')
notificar(noti_sms)