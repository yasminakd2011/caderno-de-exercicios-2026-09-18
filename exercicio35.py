nomes = []
idades = []

while True:

    print("\n=== MENU ===")
    print("1 - Cadastrar")
    print("2 - Listar maiores de 18 anos")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        nomes.append(nome)
        idades.append(idade)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == 2:

        print("\nPessoas maiores de 18 anos:")

        encontrou = False

        for i in range(len(nomes)):
            if idades[i] > 18:
                print(f"Nome: {nomes[i]} | Idade: {idades[i]}")
                encontrou = True

        if not encontrou:
            print("Nenhuma pessoa maior de 18 anos cadastrada.")

    elif opcao == 3:

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")