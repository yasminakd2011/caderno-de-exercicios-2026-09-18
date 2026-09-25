numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("\nNúmeros pares:")

for numero in numeros:
    if numero % 2 == 0:
        print(numero)