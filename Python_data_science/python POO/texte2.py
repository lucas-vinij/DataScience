class Cachorro:
    def __init__(self,raca,cor,tamanho,nome,acordado=True):
        self.raca = raca
        self.cor = cor
        self.tamanho = tamanho
        self.nome = nome
    

    def dormir(self):
        self.acordado = False
        print("Dormindo.. .")

    def latir(self):
        print("AU AU..")

    def caracteristicas(self):
        print(f"{self.raca} {self.cor} {self.tamanho} \
{self.nome} {self.acordado}")

cachorro1 = Cachorro("pincher","preto","pequeno","curika")

cachorro1.dormir()
cachorro1.latir()
cachorro1.caracteristicas()