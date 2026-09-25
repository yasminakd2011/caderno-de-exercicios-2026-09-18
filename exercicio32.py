valor = int(input("Digite o valor do saque: "))

notas20 = valor // 20
resto = valor % 20

notas1 = resto

print(f"Notas de R$ 20: {notas20}")
print(f"Notas de R$ 1: {notas1}")