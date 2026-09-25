valor_original = float(input("Digite o valor original do produto: "))

desconto = valor_original * 0.15
valor_final = valor_original - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")