# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Inicializa contadores
pares = 0
impares = 0

# Percorre os números de 1 até o número fornecido
for i in range(1, numero + 1):
    if i % 2 == 0:
        pares += 1  # Incrementa contador de pares
    else:
        impares += 1  # Incrementa contador de ímpares

# Exibe o resultado
print(f"Entre 1 e {numero}, há {pares} números pares e {impares} números ímpares.")
