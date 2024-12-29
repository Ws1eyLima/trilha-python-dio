# Operadores Aritimeticos 
valor_1 = 10
valor_2 = 3

# Adição
print("Adição", valor_1 + valor_2)

# Subtração
print("Subtração", valor_1 - valor_2)

# Multiplicação
print("Multiplicação", valor_1 * valor_2)

# Módulo
print("Módulo", valor_1 % valor_2)

# Exponenciação
print("Exponenciação", valor_1 ** valor_2)

x = (10 + 2) * 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)

# Operadores de Comparação

saldo = 200
saque = 201

# Igualdade
print("Igualdade", saldo == saque)

# Diferença
print("Diferença", saldo != saque)

# Maior que / Maior ou Igual
print("Maior que", saldo > saque)
print("Maior ou igual", saldo >= saque)

# Menor que / Menor ou Igual
print("menor que", saldo < saque)
print("menor ou igual", saldo <= saque)

# Operadores de Atribuição

saldo = 500
print (saldo)

saldo += 200
print(saldo)

saldo -= 100
print(saldo)

saldo *= 2
print(saldo)

# Operadores Logicos

# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 5000
saque = 10000
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= limite

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

# Operadores de Identidade

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

# Operadores de Associação

frutas = ["limao", "uva"]
print("laranja" in frutas)
print("limao" not in frutas)

curso = "Curso de Python"
print("Python" in curso)