saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n*** BANCO DIGITAL ***")
    print("[d] Deposito")
    print("[s] Saque")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. Apenas valores positivos são permitidos.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > limite:
            print(f"Valor excede o limite de R$ {limite:.2f} por saque.")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque:    R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n======= EXTRATO =======")
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("========================")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
