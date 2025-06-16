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
    def __init__(self, agencia, numero_da_conta, saldo=None):
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
        if self.saldo:
            if valor_a_sacar <= self.saldo and valor_a_sacar > 0:
                self.saldo -= valor_a_sacar
                print(f'Voce sacou {valor_a_sacar} \n- Novo saldo = {self.saldo} -')
            else:
                print(f'Saldo insuficiente. Seu saldo é de {self.saldo}.')

                saldo_opcional = input(f'Deseja usar o limite extra no valor de {self._limite_extra}? [s/n]').upper().strip()

                if saldo_opcional == 'S':
                    total_disponivel = self.saldo + self._limite_extra
                    if valor_a_sacar <= total_disponivel:
                        self.saldo -= valor_a_sacar
                        print(f'Você sacou {valor_a_sacar} usando o limite extra.')
                    else:
                        print(f'Nem mesmo com o limite extra você pode sacar esse valor.')

        else:
            print('NAO TEM SALDO.')        

    def depositar(self, valor_a_depositar):
        if self.saldo:
            print(f'SEU SALDO: {self.saldo}')
            self.saldo += valor_a_depositar
            print(f'Voce depositou {valor_a_depositar} \n- Novo saldo = {self.saldo} -')
            return
        print('NAO TEM SALDO.')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo=None):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def __repr__(self):
        return (f'Conta Poupanca:\n'
            f'  Banco: {self.agencia}\n'
            f'  Número: {self.numero_da_conta}\n'
            f'  Saldo: R$ {self.saldo:.2f}')
    

    def sacar(self, valor_a_sacar):
        if self.saldo:
            if valor_a_sacar > 0 and valor_a_sacar <= self.saldo:
                self.saldo -= valor_a_sacar
                print(f'Voce sacou {valor_a_sacar} \n- Novo saldo = {self.saldo} -')
                return
            print('Valor inválido para saque.')
            return
        print('NAO TEM SALDO.')
    def depositar(self, valor_a_depositar):
        if self.saldo:
            self.saldo += valor_a_depositar
            print(f'Voce depositou {valor_a_depositar} \n- Novo saldo = {self.saldo} -')
            return
        print('NAO TEM SALDO.')


