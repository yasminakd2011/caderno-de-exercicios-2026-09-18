votos = [0, 0, 0, 0, 0]

print("=== URNA ELETRÔNICA ===")
print("1 - João")
print("2 - Maria")
print("3 - José")
print("4 - Nulo")
print("5 - Branco")
print("0 - Encerrar votação")

while True:
    voto = int(input("\nDigite seu voto: "))

    if voto == 0:
        break

    if voto >= 1 and voto <= 5:
        votos[voto - 1] = votos[voto - 1] + 1
        print("Voto registrado!")
    else:
        print("Voto inválido.")

print("\n=== RESULTADO ===")

print(f"João: {votos[0]} voto(s)")
print(f"Maria: {votos[1]} voto(s)")
print(f"José: {votos[2]} voto(s)")
print(f"Nulos: {votos[3]} voto(s)")
print(f"Brancos: {votos[4]} voto(s)")

maior = max(votos[0], votos[1], votos[2])

if maior == 0:
    print("Nenhum candidato recebeu votos.")
elif votos[0] == maior and votos[1] != maior and votos[2] != maior:
    print("Vencedor: João")
elif votos[1] == maior and votos[0] != maior and votos[2] != maior:
    print("Vencedor: Maria")
elif votos[2] == maior and votos[0] != maior and votos[1] != maior:
    print("Vencedor: José")
else:
    print("Houve empate entre os candidatos.")