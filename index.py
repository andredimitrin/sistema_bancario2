# Lista para armazenar as contas correntes
contas_correntes = []

# Dicionário para armazenar as informações dos usuários
usuarios = {}

# Variável para controlar o número da conta sequencial
numero_conta_sequencial = 1

def cliente(nome, data_nascimento, cpf, endereco):
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    return cpf

def conta_corrente(saldo=0, limite=500):
    global numero_conta_sequencial
    numero_conta = numero_conta_sequencial
    numero_conta_sequencial += 1

    return {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "saldo": saldo,
        "limite": limite,
        "extrato": "",
        "numero_saques": 0,
        "LIMITE_SAQUES": 3
    }

def saque(numero_conta, valor_saque):
    for conta, cpf_usuario in contas_correntes:
        if conta["numero_conta"] == numero_conta:
            saldo = conta["saldo"]
            extrato = conta["extrato"]
            limite = conta["limite"]
            numero_saques = conta["numero_saques"]
            LIMITE_SAQUES = conta["LIMITE_SAQUES"]

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
                conta["saldo"] = saldo
                conta["extrato"] = extrato
                conta["numero_saques"] = numero_saques
                return saldo, extrato

    print("Conta corrente não encontrada.")
    return None, None

def deposito(numero_conta, valor_deposito):
    for conta, cpf_usuario in contas_correntes:
        if conta["numero_conta"] == numero_conta:
            saldo = conta["saldo"]
            extrato = conta["extrato"]

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print("Depósito realizado com sucesso!")
                conta["saldo"] = saldo
                conta["extrato"] = extrato
                return saldo, extrato

    print("Conta corrente não encontrada.")
    return None, None

def extrato(numero_conta):
    for conta, cpf_usuario in contas_correntes:
        if conta["numero_conta"] == numero_conta:
            saldo = conta["saldo"]
            extrato = conta["extrato"]
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
            return saldo, extrato

    print("Conta corrente não encontrada.")
    return None, None

def criar_conta(nome, data_nascimento, cpf, endereco):
    cpf_usuario = cliente(nome, data_nascimento, cpf, endereco)
    conta = conta_corrente()
    contas_correntes.append((conta, cpf_usuario))
    print("Conta criada com sucesso!")

def listar_contas():
    if contas_correntes:
        print("=== LISTA DE CONTAS ===")
        for conta, cpf_usuario in contas_correntes:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"CPF do Titular: {cpf_usuario}")
            print(f"Saldo: R$ {conta['saldo']:.2f}")
            print("===============")
    else:
        print("Não existem contas cadastradas.")

def listar_usuarios():
    if usuarios:
        print("=== LISTA DE USUÁRIOS ===")
        for cpf, info in usuarios.items():
            print(f"Nome: {info['nome']}")
            print(f"Data de Nascimento: {info['data_nascimento']}")
            print(f"CPF: {cpf}")
            print(f"Endereço: {info['endereco']}")
            print("===============")
    else:
        print("Não existem usuários cadastrados.")

def main():
    while True:
        menu = """
        [1] Criar conta
        [2] Criar usuário
        [3] Listar contas
        [4] Listar usuários
        [5] Realizar depósito
        [6] Realizar saque
        [7] Consultar extrato
        [8] Sair

        => """

        opcao = input(menu)

        if opcao == "1":
            nome = input("Digite o nome do titular: ")
            data_nascimento = input("Digite a data de nascimento do titular (DD/MM/AAAA): ")
            cpf = input("Digite o CPF do titular: ")
            endereco = input("Digite o endereço (logradouro, bairro, cidade/estado): ")
            criar_conta(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
            cpf = input("Digite o CPF do usuário: ")
            endereco = input("Digite o endereço do usuário (logradouro, bairro, cidade/estado): ")
            cliente(nome, data_nascimento, cpf, endereco)

        elif opcao == "3":
            listar_contas()

        elif opcao == "4":
            listar_usuarios()

        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            valor_deposito = float(input("Digite o valor do depósito: "))
            deposito(numero_conta, valor_deposito)

        elif opcao == "6":
            numero_conta = int(input("Digite o número da conta: "))
            valor_saque = float(input("Digite o valor do saque: "))
            saque(numero_conta, valor_saque)

        elif opcao == "7":
            numero_conta = int(input("Digite o número da conta: "))
            extrato(numero_conta)

        elif opcao == "8":
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
