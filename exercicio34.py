frase = input("Digite uma frase: ")

quantidade_a = 0
quantidade_palavras = 0
dentro_da_palavra = False

for caractere in frase:

    if caractere == "a" or caractere == "A":
        quantidade_a = quantidade_a + 1

    if caractere != " " and dentro_da_palavra == False:
        quantidade_palavras = quantidade_palavras + 1
        dentro_da_palavra = True

    elif caractere == " ":
        dentro_da_palavra = False

print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Quantidade de letras A: {quantidade_a}")