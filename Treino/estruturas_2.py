# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [2, 4, 6, 8, 10]

# for a in numero:
#     if a in pares:
#         print(a)

# for numero in range(0, 103, 3):
#     print(numero, end=" ")

# opcao = -1

# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n [0] Sair \n:"))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo extrato")
# else:
#     print("Obrigado por usar nosso banco")


while True :
    numero= int(input("Informe um numero: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)