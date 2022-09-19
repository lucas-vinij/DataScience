def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor Sacado {}".format(valor))

    print("FIM..")

sacar(100)


def depositar(valor):
    saldo = 500 
    saldo += valor
    print("Saldo atual {}".format(saldo))

depositar(100)