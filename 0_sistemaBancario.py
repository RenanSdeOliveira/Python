import textwrap

def menu():
    menu = """\n
    == Naner Bank ==
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair
    ================
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso! ")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            CC:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

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

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Você finalizou a sessão.")
            break
         
        else:
            print("Operação Abortada, selecione novamente a opção desejada.")
         
main()
