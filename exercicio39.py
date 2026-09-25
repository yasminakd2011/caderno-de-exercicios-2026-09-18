# Exercício 40 - Mini-Sistema Bancário Definitivo

nome = ""
conta = ""
saldo = 0.0
conta_criada = False

while True:

    print("\n=== SISTEMA BANCÁRIO ===")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato / Ver Saldo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        if conta_criada:
            print("A conta já foi criada.")

        else:
            nome = input("Digite o nome do titular: ")
            conta = input("Digite o número da conta: ")

            saldo = 0.0
            conta_criada = True

            print("Conta criada com sucesso!")

    elif opcao == 2:

        if not conta_criada:
            print("É necessário criar uma conta primeiro.")

        else:
            valor = float(input("Digite o valor do depósito: "))

            if valor > 0:
                saldo = saldo + valor
                print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")

    elif opcao == 3:

        if not conta_criada:
            print("É necessário criar uma conta primeiro.")

        else:
            valor = float(input("Digite o valor do saque: "))

            if valor <= 0:
                print("O valor do saque deve ser positivo.")

            elif valor > saldo:
                print("Saldo insuficiente.")

            else:
                saldo = saldo - valor
                print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")

    elif opcao == 4:

        if not conta_criada:
            print("É necessário criar uma conta primeiro.")

        else:
            print("\n=== EXTRATO ===")
            print(f"Titular: {nome}")
            print(f"Conta: {conta}")
            print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 5:

        print("Obrigado por utilizar o sistema bancário.")
        break

    else:
        print("Opção inválida.")
