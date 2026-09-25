import random

numero_secreto = random.randint(1, 10)

tentativas = 0

print("Pensei em um número entre 1 e 10!")

while True:
    palpite = int(input("Tente adivinhar: "))

    tentativas = tentativas + 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break

    elif palpite < numero_secreto:
        print("Maior!")

    else:
        print("Menor!")

print(f"Você precisou de {tentativas} tentativa(s).")
