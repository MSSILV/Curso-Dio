import textwrap


def main():
    LIMITE = 500 
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saques_realizados = 0
    saldo = 0
    extrato = ''
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == 'D':
            valor = float(input('Informe o valor de Depósito: ').replace(',','.'))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == 'S':
            valor = float(input('Informe o valor de Saque: ').replace(',','.'))
            saldo, extrato, saques_realizados = saque(
                valor=valor, 
                saldo=saldo, 
                extrato=extrato,
                limite=LIMITE,
                limite_saques=LIMITE_SAQUES, 
                numero_saques=saques_realizados)
        
        elif opcao == 'E':
            Extrato(saldo, extrato=extrato)
        
        elif opcao == 'LC':
            listar_contas(contas)


        elif opcao == 'NC':
            numero_conta =len(contas)+1
            conta = Cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'NU':
            cadastrar_usuario(usuarios)

        elif opcao =='Q':
            print('Obrigado por ser nosso cliente')
            print('Volte Sempre!!!')
            break

        else:
            print('opção invalida, tente novamente')


def menu():
    menu = """\n
    ===============MENU===================
    Digite a operação que deseja realizar:
    [D]\tDepósito
    [S]\tSaque
    [E]\tExtrato
    [LC]\tListar Contas
    [NU]\tNovo Usuário
    [NC]\tNova Conta
    [Q]\tsair
    ==> """
    print("======================================")
    return input(textwrap.dedent(menu)).upper()

     
def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_insuficiente = valor > saldo
    limite_superior = valor >limite
    excedeu_limite_saques = numero_saques >= limite_saques
    if saldo_insuficiente:
        print('A operação falhou, saldo insuficiente!')
    
    elif limite_superior:
        print('A operação falhou, valor informado é maior do que o limite diario!')

    elif excedeu_limite_saques:
        print('A operação falhou, limite diario de saques atingido!')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com Sucesso!')

    else:
        print('A operação falhou, valor informado é inválido!')
    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato):
    if valor >0:
            saldo += valor
            extrato += f'Deposito:\tR$ {valor:.2f}\n'
            print('Depósito realizado com Sucesso!')
            
    else:
        print('A operação falhou, valor informado é inválido!')
    return saldo, extrato


def Extrato(saldo,/, *, extrato):
    print('==============EXTRATO=================')
    print("Sem Movimentações realizadas" if not extrato else extrato)
    print(f'Saldo Disponivel R${saldo:.2f} ')
    

def cadastrar_usuario(usuarios):
    cpf = input('Digite o número do CPF (Somente Números): ')
    usuario = fitrar_usuario(cpf, usuarios)
    if usuario:
        print('Existe um usuário cadastrado com esse CPF.')
        return
    nome = input('Informe o nome Completo: ')
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input('Informe o endereço (Logradouro, nº - Bairro - Cidade)/Estado "XX": ')
    usuarios.append({"nome":nome, "cpf":cpf, "Data Nascimento":data_nascimento, "endereco":endereco})
    print('Usuário cadastrado com sucesso!')
    

def Cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o número do CPF (Somente Números): ')
    usuario = fitrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso!!")

        dados_conta =f"""
            Titular:\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Agencia:\t{agencia}
            C/C:\t\t{numero_conta}
        """
        print(textwrap.dedent(dados_conta))
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print('Usário não cadastrado, realize o cadastro primeiro.')
    

def fitrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas (contas):
    for conta in contas:
        dados_conta= f"""
            Titular:\t{conta['usuario']['nome']}
            CPF:\t\t{conta['usuario']['cpf']}
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
        """
        print(textwrap.dedent(dados_conta))
        
    
main()
