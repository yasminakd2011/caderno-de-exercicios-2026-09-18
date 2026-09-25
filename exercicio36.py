produtos = []
quantidades = []

while True:

    print("\n=== GERENCIADOR DE ESTOQUE ===")
    print("1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))

        encontrado = False

        for i in range(len(produtos)):
            if produtos[i].lower() == nome.lower():
                quantidades[i] = quantidades[i] + quantidade
                encontrado = True
                print("Quantidade adicionada ao produto existente.")

        if not encontrado:
            produtos.append(nome)
            quantidades.append(quantidade)
            print("Produto adicionado ao estoque.")

    elif opcao == 2:

        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade para retirar: "))

        encontrado = False

        for i in range(len(produtos)):
            if produtos[i].lower() == nome.lower():
                encontrado = True

                if quantidade <= quantidades[i]:
                    quantidades[i] = quantidades[i] - quantidade
                    print("Baixa realizada com sucesso.")
                else:
                    print("Estoque insuficiente.")

        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 3:

        print("\n=== ESTOQUE ===")

        if len(produtos) == 0:
            print("Estoque vazio.")
        else:
            for i in range(len(produtos)):
                print(f"{produtos[i]}: {quantidades[i]} unidade(s)")

    elif opcao == 4:

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")