
# class Eletrodomestico():
#     def __init__(self,valor, marca, ano):
#         self.valor = valor
#         self.marca = marca
#         self.ano = ano 

#     def propaganda(self):
#         print("Ta barato...")

# class Celular(Eletrodomestico):
#     def __init__(self,valor, marca,ano, camera,so, ia):
#         self.camera = camera 
#         self.so = so 
#         self.ia = ia
#         super().__init__(valor,marca,ano)

#     def inteligencia(self):
#         print(f"{'Celular com IA'if self.ia else 'Velho pra caramba'}")


# celular1 = Celular(1200,"samsung",2022,"50mps","IOS",False)
# print(celular1.so)
# celular1.propaganda()
# celular1.inteligencia()

class Time():
    def __init__(self, estadio, torcida, tecnico):
        self.estadio = estadio
        self.torcida = torcida
        self.tecnico = tecnico

    def gol(self):
        print("Gooooolll!!!")

class Flamengo(Time):
    def __init__(self, estadio, torcida, tecnico, gabigol, patamar):
        super().__init__(estadio,torcida, tecnico)
        self.gabigol = gabigol 
        self.patamar = patamar 


    def acima_nivel(self):
        print(f"{'Em outro patamar, exxquece' if self.patamar else 'Fracos'}")

    def tem_ou_nao(self):
        print(f"{'Infelizmente ele está aqui'if self.gabigol else 'Ainda bem não tem Gabigol'}")


flamidia = Flamengo("fla_estadio",20000,"JJ",False,True)
flamidia.acima_nivel()
flamidia.tem_ou_nao()