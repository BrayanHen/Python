class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def ver_saldo(self):
        print(f'Saldo: {self.saldo}')

pessoa1=ContaBancaria(100)
pessoa1.depositar(100)
pessoa1.sacar(200)
pessoa1.ver_saldo()