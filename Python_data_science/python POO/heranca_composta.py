from ast import Or


class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        

class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass
    
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        
        print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

# gato = Gato(4,"preto")
# print(gato.cor_pelo)

ornitorrinco = Ornitorrinco(nro_patas=4,cor_pelo="vermelho",cor_bico="preto")
print(ornitorrinco.cor_pelo)
print(ornitorrinco.cor_bico)