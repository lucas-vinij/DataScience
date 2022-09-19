#|Dirigir
idade = int(input("Digite sua idade: "))

if idade < 18:
    permissao = 18 - idade
    print("Não pode dirigir, falta {} anos para ser PERMITIDO".format(permissao))

else:
    print("Você estar apto para dirigir")

saldo = 2000.01
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
    
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade =int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Permissão TRUE")

elif idade == IDADE_ESPECIAL:
    print("Pode assistir AULAS")

elif idade < MAIOR_IDADE:
    print("Permissão FALSE")

else:
    print("Valor NÃO Identificado")

IDADE_CARTEIRA = 18
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("PODE TIRAR CARTEIRA")

elif idade < 18:
    if idade == 12:
        print("PODE ASSISTIR AULAS")
    else:
        print("NÃO PODE NADA")