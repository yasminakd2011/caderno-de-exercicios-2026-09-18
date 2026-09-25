nomes = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))

    nomes.append(nome)
    notas.append(nota)

print("\nResultado dos alunos:")

for i in range(3):
    print(f"\nAluno: {nomes[i]}")
    print(f"Nota: {notas[i]:.2f}")

    if notas[i] >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")