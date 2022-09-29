from distutils import core


class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Beeeeeeeeeeeee")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmmm")

    def get_cor(self):
        return self.cor

    # def __str__(self):
    #     return f"Bicicleta: {self.cor},{self.modelo}, {self.ano}, {self.valor}"        
    #     {self.valor}

    # def __str__(self):
        # return f"{self.__class__.__name__}: {[f'{chave}={valor}'chave for chave, valor in self.__d]}"

b1 = Bicicleta("vermelha","caloi",2022,600)

b1.buzinar()
b1.correr()
b1.parar()
print("\n",b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark",2000, 189)
Bicicleta.buzinar(b2)

print(b2)



