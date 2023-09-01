menu = """
== Naner Bank ==
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [0] Sair
================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: $ {valor:.2f}\n"
            print("Você depositou: ", valor)
            
        else:
            print("Operação abortada! O valor é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor a sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação abortada! Você não tem saldo suficiente para essa transação.")
        
        elif excedeu_limite:
            print("Operação abortada! O valor do saque excedo o limite da transação.")
        
        elif excedeu_saques:
            print("operação abortada! Número de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: $ {valor:.2f}\n"
            numero_saques += 1
            print("Você sacou: ", valor)
        
        else:
            print("Operação abortada! o valor é inválido.")

    elif opcao == "3":
        print("\n ========= Inicio do Extrato =========")
        print("Não foram feitas movimentações." if not extrato else extrato)
        print(f"\nSaldo: $ {saldo:.2f}")
        print("\n ========= Fim do Extrato =========")

    elif opcao == "0":
        print("Você finalizou a sessão.")
        break

    else:
        print("Operação Abortada, selecione novamente a opção desejada.")
