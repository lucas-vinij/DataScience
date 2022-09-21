frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

matriz = [
    [1, "a, 2"],
    ["b", 3, 4],
    [5, 5, "c"]
]

matriz[0] #[1,"a",2]
matriz[0,0] #1
matriz[0][-1] #2
matriz[-1][-1] #c


lista = ["p","y","t","h","o","n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice: {carro}}")

numeros = [1,30, 21,2,9,65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]
