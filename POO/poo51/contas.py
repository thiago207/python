from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self):
        self.agencia = None
        self.numero_da_conta = None
        self.saldo = None
    
    @abstractmethod
    def sacar(self):
        ...
    
    @abstractmethod
    def depositar(self):
        ...
    
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self._limite_extra = 300


    def __repr__(self):
        return (f'Conta Corrente:\n'
            f'  Banco: {self.agencia}\n'
            f'  Número: {self.numero_da_conta}\n'
            f'  Saldo: R$ {self.saldo:.2f}')



    def sacar(self, valor_a_sacar):

        print(f'SEU SALDO: {self.saldo}')

        if valor_a_sacar <= self.saldo:
            self.saldo -= valor_a_sacar
            print(f'Voce sacou {valor_a_sacar} \n- Novo saldo = {self.saldo}')
        else:
            print(f'Saldo insuficiente. Seu saldo é de {self.saldo}.')

            saldo_opcional = input(f'Deseja usar o limite extra no valor de {self._limite_extra}? [s/n]').upper().strip()

            if saldo_opcional == 'S':
                total_disponivel = self.saldo + self._limite_extra
                #print(f'{total_disponivel} - Novo saldo.')
                if valor_a_sacar <= total_disponivel:
                    self.saldo -= valor_a_sacar
                    print(f'Você sacou {valor_a_sacar} usando o limite extra.')
                else:
                    print(f'Nem mesmo com o limite extra você pode sacar esse valor.')        

    def depositar(self, valor_a_depositar):
        print(f'SEU SALDO: {self.saldo}')
        self.saldo += valor_a_depositar
        print(f'Voce depositou {valor_a_depositar} \n- Novo saldo = {self.saldo}')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def __repr__(self):
        return (f'Conta Poupanca:\n'
            f'  Banco: {self.agencia}\n'
            f'  Número: {self.numero_da_conta}\n'
            f'  Saldo: R$ {self.saldo:.2f}')
    

    def sacar(self, valor_a_sacar):
        print(f'{self.saldo}')
        self.saldo -= valor_a_sacar
        print(f'Voce sacou {valor_a_sacar} \n- Novo saldo = {self.saldo}')

    def depositar(self, valor_a_depositar):
        print(f'{self.saldo}')
        self.saldo += valor_a_depositar
        print(f'Voce deositou {valor_a_depositar} \n- Novo saldo = {self.saldo}')


