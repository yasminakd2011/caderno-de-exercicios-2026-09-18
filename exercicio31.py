notas = []
soma = 0

for i in range(5):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))

    notas.append(nota)
    soma = soma + nota

media = soma / len(notas)

print(f"\nMédia da turma: {media:.2f}")

acima_da_media = 0

for nota in notas:
    if nota > media:
        acima_da_media = acima_da_media + 1

print(f"Alunos acima da média: {acima_da_media}")