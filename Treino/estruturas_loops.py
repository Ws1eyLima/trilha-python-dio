def sacar(valor):

    saldo = 500
    saldo -= valor

    if saldo >= valor:
        print("Valor sacado,seu saldo agora é: ", saldo)
    else:
        print("Nao foi possivel realizar o saque")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor depositado com sucesso")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as teoricas")
else:
    print("Ainda nao pode tirar a CNH")

saldo = 500
cheque_especial = 100
conta_normal = False
conta_universitaria = True
saque = 600

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o cheque especial")
    else:
        print("Nao foi possivel realizar o saque")
elif conta_universitaria:

    if saldo >= saque:
        print("saque realizado com sucesso")
    else:
        print("Saque indisponivel")

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")