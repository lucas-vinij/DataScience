valores = input().split()

carro = 12

horas_viagem = int(valores[0])
velocidade_media = int(valores[1])

distancia_percorrida = horas_viagem * velocidade_media

litros = distancia_percorrida / 12
print(f"{litros:.3f}")