from inspect import CORO_SUSPENDED


class Sorvete:
    def __init__(self, sabor, cor, preco):
        self.sabor = sabor
        self.cor = cor
        self.preco = preco

    def derreter(self):
        return f"Derretendo o sorvete de {self.sabor}"

    def comer(self):
        return f"yummy ..."



nestle = Sorvete("flocos","branco com preto",16)

print(nestle.derreter())

print(nestle.comer())
