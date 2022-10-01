class Conta:
    
    def __init__(self,nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo

    def depositar(self, valor):
        # .. .
        self.valor += valor

    def sacar(self, valor):
        # ...
        self.saldo -= valor


# errado fazer isto
conta = Conta("1022",100)
conta._saldo += 100
print(conta._saldo)

conta.depositar(100)