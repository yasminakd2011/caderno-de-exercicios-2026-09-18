numeros = []

for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

busca = int(input("\nDigite o número que deseja buscar: "))

encontrado = False

for i in range(len(numeros)):
    if numeros[i] == busca:
        print(f"O número foi encontrado na posição {i}.")
        encontrado = True

if not encontrado:
    print("O número não está na lista.")