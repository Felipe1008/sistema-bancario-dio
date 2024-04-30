def menu():
    print(
        '''
        ====== MENU ======
            1 - Depositar
            2 - Sacar
            3- Extrato
            4 - Nova Conta
            5 - Listar Contas
            6 - Novo Usuário
            0 - Sair
        ==================
        '''
    )
    
    return int(input("Digite a operação que deseja realizar: "))

def sacar(*,saldo, valor, extrato, limite, limite_saque, numero_saques):
    if valor <= saldo:
        if valor <= limite:
            if numero_saques < limite_saque:
                saldo -= valor;
                extrato += f'Saque de R${valor:.2f}\n'
                print('\n=== Saque realizado com sucesso! ===')
                numero_saques += 1
                print(f"\n NUMERO SAQUES: {numero_saques}")
            else:
                print('\n@@@ Você atingiu a sua quantidade máxima de saques diários. @@@')
        else:
            print(f'\n@@@ Seu limite é de R${limite}. Aumente seu limite para sacar essa quantia. @@@')
    else:
        print(f'\nSaldo insuficiente!')
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R${valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Insira um valor válido. @@@')
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("===== Movimentações =====\n")
    print("Não foram realizadas movimentações." if not(extrato) else extrato)
    print("="*25);
    print(f"\nSaldo: R${saldo:.2f}\n");
    print("="*25);

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@ CPF de usuário já cadastrado! @@@")
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimeento = input("Digite a data nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimeento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! === ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("@@@ Usuário não encontrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t {conta["agencia"]}
            C/C:\t {conta["numero_conta"]}
            Usuário:\t {conta["usuario"]}
       """
        print("="*100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu();

        if opcao == 1:
            valor = float(input('Qual valor deseja depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            if numero_saques < LIMITE_SAQUES:
                valor = float(input('Qual valor deseja sacar: '))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                limite_saque = LIMITE_SAQUES,
                numero_saques = numero_saques
            )
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 5:
            listar_contas(contas)
        
        elif opcao == 6:
            criar_usuario(usuarios)
        
        elif opcao == 0:
            print("\nObrigado por utilizar nossos serviços!")
            break
            
        else:
            print('Digite uma opção válida. Tente novamente!')

main()