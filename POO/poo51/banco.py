from contas import ContaCorrente, ContaPoupanca
from pessoas import Cliente

class Banco:
    def __init__(self, nome, agencias=None):
        self.nome = nome
        self._clientes = []
        self._contas = []
        self._agencias = agencias if agencias else []
    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def autenticar(self, cliente, conta):
        if cliente not in self._clientes:
            print('Cliente não é do banco.')
            return False

        if conta not in self._contas:
            print('Conta não é do banco.')
            return False

        if cliente.conta != conta:
            print('Esta conta não pertence a este cliente.')
            return False

        if conta.agencia not in self._agencias:
            print('Agência não pertence a este banco.')
            return False

        return True

    def sacar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.sacar(valor)
        else:
            print('Falha na autenticação. Saque não autorizado.')
    

conta_p1 = ContaCorrente('ITAU', 1234, 1000)
cliente1 = Cliente('Thiago', 18, conta_p1)

# Criando o banco
banco = Banco('Meu Banco', agencias=['ITAU', 'NUBANK'])
banco.adicionar_cliente(cliente1)
banco.adicionar_conta(conta_p1)

banco.sacar(cliente1, conta_p1, 300)