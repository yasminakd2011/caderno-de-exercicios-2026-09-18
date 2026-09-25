quantidade = 0
soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    quantidade = quantidade + 1
    soma = soma + numero

    numero = int(input("Digite um número (0 para parar): "))

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")