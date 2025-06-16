from contas import ContaCorrente, ContaPoupanca
from pessoas import Cliente
from banco import Banco


conta1 = ContaCorrente('ITAU', 1234, 999.8)
cliente1 = Cliente('Thiago', 18, conta1)
banco1 = Banco('Meu Banco', agencias=['ITAU'])
banco1.adicionar_cliente(cliente1)
banco1.adicionar_conta(conta1)
banco1.autenticar(cliente1, conta1)


print(banco1)
