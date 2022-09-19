saldo = 2000
saque = 200

#if ternario
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

idade = int(input("Digite sua idade: "))
resultado = "IMPOSSIVEL" if idade < 18 else "PERMITIDO"
print(f"{resultado} você DIRIGIR")

CELULAR = 500
banco = int(input("Digite seu saldo: "))
status = "PODE" if banco >= CELULAR else "NÃO PODE"
print(f"Você {status} comprar Celular")