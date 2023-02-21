'''
                                Objetivo Geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

                                Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

                                Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos 
preocupar em identificar qual é o número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

                                Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando 
que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

                                Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido o saldo atual da conta. 
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
'''

menu = """
  Digite a operação que deseja realizar:
    [D] Depósito
    [S] Saque
    [E] Extrato
    [Q] sair
"""

LIMITE_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3
numero_saque = 3
saldo = 0
extrato = ''
saques = []
depositos = []


while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        print('Opção escolhida Depósito.')
        valor_deposito = int(input('Digite o valor do depósito: '))
        saldo += valor_deposito
        depositos.append(valor_deposito)


    elif opcao == 'S':
        print('Opção escolhida Saque.')

        if 0 < numero_saque:
            valor_saque = int(input('Digite o valor do Saque: '))

            if valor_saque <= LIMITE_SAQUE:
                if saldo >= valor_saque:
                    print('Saque Realizado com sucesso!!!')
                    saldo -= valor_saque
                    numero_saque -= 1
                    saques.append(valor_saque)

                else:
                    print("Saldo Insuficiente, verifique o Saldo!")

            else:
                print(f'O valor solicitado (R${valor_saque:.2f}) ultrapassa o limite de saque de R${LIMITE_SAQUE:.2f}. ')
                
        else:
            print(f'Quantidade de Saques realizados hoje utrapassou o limite de {LIMITE_SAQUE_DIARIO} saques diarios.')


    elif opcao == 'E':
        print('Opção escolhida Extrato.\n')
        print('DEPOSITOS:\n')

        for i, v, in enumerate(depositos):
            print(f'{i+1}º Deposito, valor de R${v:.2f}.')
        
        print('\nSAQUES:\n')
        
        for i, v, in enumerate(saques):
            print(f'{i+1}º Saque, valor de R${v:.2f}.')

        print(f'\nSaldo disponivel: R${saldo:.2f}.')


    elif opcao == 'Q':
        print('Obrigado por ser nosso cliente!!!')
        break


    else:
        print('opção invalida, tente novamente')


