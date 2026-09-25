# Exercício 39 - Reservas de Cinema

assentos = [False] * 10

while True:

    print("\n=== MAPA DE ASSENTOS ===")

    for i in range(len(assentos)):
        if assentos[i]:
            print(f"[{i}: OCUPADO]", end=" ")
        else:
            print(f"[{i}: LIVRE]", end=" ")

    print()

    poltrona = int(input("\nDigite o número da poltrona (-1 para sair): "))

    if poltrona < 0:
        print("Sistema encerrado.")
        break

    if poltrona > 9:
        print("Poltrona inválida.")
        continue

    if assentos[poltrona]:
        print("Ocupada.")
    else:
        assentos[poltrona] = True
        print("Reservada.")
