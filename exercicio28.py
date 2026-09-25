numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista principal:")
print(numeros)

print("\nLista de pares:")
print(pares)

print("\nLista de ímpares:")
print(impares)