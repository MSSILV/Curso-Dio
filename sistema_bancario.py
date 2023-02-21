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
LIMITE = 500 
LIMITE_SAQUES = 3
saques_realizados = 0
saldo = 0
extrato = ''

menu = """
  Digite a operação que deseja realizar:
    [D] Depósito
    [S] Saque
    [E] Extrato
    [Q] sair
==>"""

while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        print('Operação escolhida Depósito')
        valor = float(input('Informe o valo de Depósito: '))

        if valor >0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print('Depósito realizado com Sucesso!')
            
        else:
            print('A operação falhou, valor informado é inválido!')
       

    elif opcao == 'S':
        valor = float(input('Digite o valor que deseja sacar: '))
       
        saldo_insuficiente = valor > saldo
        limite_superior = valor >LIMITE
        excedeu_limite_saques = saques_realizados >= LIMITE_SAQUES

        if saldo_insuficiente:
            print('A operação falhou, valor informado é maior do que o saldo disponivel!')
        
        elif limite_superior:
            print('A operação falhou, valor informado é maior do que o limite diario!')

        elif excedeu_limite_saques:
            print('A operação falhou, limite diario de saques atingido!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            saques_realizados += 1
            print('Saque realizado com Sucesso!')

        else:
            print('A operação falhou, valor informado é inválido!')
       
    
    elif opcao == 'E':
        print('=-='*15)
        print("Sem Movimentações realizadas" if not extrato else extrato)
        print(f'Saldo Disponivel R${saldo:.2f} ')
        print('=-='*15)

        
    elif opcao == 'Q':
        print('Obrigado por ser nosso cliente')
        print('Volte Sempre!!!')
        break

       
    else:
        print('opção invalida, tente novamente')
        
        
