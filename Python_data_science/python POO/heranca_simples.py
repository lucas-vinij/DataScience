


class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor    
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    def __init__(self, cor, placa, numero_rodas,automatico):
        super().__init__(cor, placa, numero_rodas)
        self.automatico = automatico

    def estacionar(self):
        print(f"{'Estacionando' if self.automatico else 'Impossivel'}")
    

class Caminhao(Veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):

        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Estou Carregado' if self.carregado else 'NÃO estou carregado'}")


moto = Motocicleta("preta","ABC123",2)
moto.ligar_motor()


carro = Carro("Branco","ADV342",4,False)
carro.ligar_motor()
carro.estacionar()

caminhao = Caminhao("Roxo","GKF496",8,True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(caminhao)