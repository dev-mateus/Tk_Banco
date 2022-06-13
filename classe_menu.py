from classe_cliente import *
from classe_conta import *

while input('Deseja continuar? Sim ou Não (S / N):') == 'S':

    op = input('1-Cria cadastro\n2-Acesso cliente\n')
    if op == '1':
        p1 = Cliente(nome=input('Nome:\n'), cpf=input('CPF:\n'), dataNasc=input('Data de Nascimento:\n'))
        c1 = Conta(p1, num=input('Numero da conta:\n'))

        p1 = Cliente(nome=input('Nome:\n'), cpf=input('CPF:\n'), dataNasc=input('Data de Nascimento:\n'))
        c1 = Conta(p1, num=input('Numero da conta:\n'))

    elif op == '2':
        op2 = input('1-Exrato\n2-Saque\n3-Deposito\n4-Sair\n')
        while op2 != 4:
            if op2 == '1':
                c1.extrato()
                op2 = input('1-Exrato\n2-Saque\n3-Deposito\n4-Sair\n')

            elif op2 == '2':
                rs = float(input('Digite o valor a ser sacado:\n'))
                c1.saque(rs)
                op2 = input('1-Exrato\n2-Saque\n3-Deposito\n4-Sair\n')

            elif op2 == '3':
                rs = float(input('Digite o valor a ser depositado:\n'))
                c1.deposito(rs)
                op2 = input('1-Exrato\n2-Saque\n3-Deposito\n4-Sair\n')

            else:
                print('Volte sempre!')
                break