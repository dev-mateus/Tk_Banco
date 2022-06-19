from classe_cliente import *
from classe_conta import *
# from classe_historico import *
from tkinter import *

'''
p1 = Cliente(nome='Mateus', cpf='12345678', dataNasc='06/05/1988')
c1 = Conta(p1, num='123-4')

p2 = Cliente(nome='Rodrigo', cpf='12345690', dataNasc='02/04/1987')
c2 = Conta(p2, num='123-6')

c1.deposito(500)
c1.transfere_para(50,c2)

c1.extrato()
c2.extrato()'''
clientes = []
contas = []


def cadastrar_cliente():
    global clientes, contas, nome_ent, cpf_ent, dataNasc_ent, num_ent
    clientes.append(Cliente(nome=nome_ent.get(), cpf=cpf_ent.get(), dataNasc=dataNasc_ent.get()))

    for i in range(len(clientes)):
        if clientes[i].cpf == cpf_ent.get():
            contas.append(Conta(clientes[i], num=num_ent.get()))


def entrar():
    global contas, num_conta_ent
    for i in range(len(contas)):
        if contas[i].num == num_conta_ent.get():
            tela_cliente.pack_forget()
            tela_cliente_dados.grid(row=0, column=0, sticky=NS)
            tela_cliente_menu.grid(row=0, column=1)
            tela_cliente_extrato.grid(row=1, column=0, columnspan=2, sticky=EW)
            cliente_nome['text'] = 'Nome: ' + clientes[i].nome
            cliente_cpf['text'] = 'CPF: ' + clientes[i].cpf
            cliente_dataNasc['text'] = 'Data Nasc.: ' + clientes[i].dataNasc
            cliente_num['text'] = 'N° da conta: ' + contas[i].num
            cliente_saldo['text'] = 'Saldo: ' + str(contas[i].saldo)
            extrato_saida['text'] = ''



def cliente_depositar():
    global contas, num_conta_ent
    for i in range(len(contas)):
        if contas[i].num == num_conta_ent.get():
            contas[i].deposito(float(valor_ent.get()))
            cliente_saldo['text'] = 'Saldo: ' + str(contas[i].saldo)
            tela_cliente_deposito.grid_forget()


def cliente_sacar():
    global contas, num_conta_ent
    for i in range(len(contas)):
        if contas[i].num == num_conta_ent.get():
            contas[i].saque(float(saque_ent.get()))
            cliente_saldo['text'] = 'Saldo: ' + str(contas[i].saldo)
            tela_cliente_saque.grid_forget()


def cliente_transferir():
    global contas, num_conta_ent, transferencia_conta_ent
    for j in range(len(contas)):
        if contas[j].num == transferencia_conta_ent.get():
            conta_destino = contas[j]

    for i in range(len(contas)):
        if contas[i].num == num_conta_ent.get():
            contas[i].transfere_para(float(transferencia_ent.get()), conta_destino)
            cliente_saldo['text'] = 'Saldo: ' + str(contas[i].saldo)
            tela_cliente_transferencia.grid_forget()


def cliente_imprimir_extrato():
    global contas, num_conta_ent
    for i in range(len(contas)):
        if contas[i].num == num_conta_ent.get():
            contas[i].historico.transacoes_bancarias()
            extrato_saida['text'] = contas[i].historico.msg


root = Tk()
root.minsize(width=500, height=500)
tela_login = LabelFrame(root, text='Login', font='Verdana 16')
cadastro_cliente = LabelFrame(root, text='Cadastro', font='Verdana 16')
tela_cliente = LabelFrame(root, text='login', font='Verdana 16')
tela_cliente_dados = LabelFrame(root, text='dados', font='Verdana 16')
tela_cliente_menu = LabelFrame(root, text='menu', font='Verdana 16')

cliente = Button(tela_login, text='Cliente', font='Verdana 20', width=10,
                 command=lambda: [tela_cliente.pack(), tela_login.pack_forget()])
funcionario = Button(tela_login, text='Funcionário', font='Verdana 20', width=10,
                     command=lambda: [cadastro_cliente.pack(), tela_login.pack_forget(),
                                      tela_cliente_dados.pack_forget()])

nome = Label(cadastro_cliente, text='Nome: ', font='Verdana 20')
cpf = Label(cadastro_cliente, text='CPF: ', font='Verdana 20')
dataNasc = Label(cadastro_cliente, text='Data Nasc.: ', font='Verdana 20')
num = Label(cadastro_cliente, text='N° da conta: ', font='Verdana 20')

nome_ent = Entry(cadastro_cliente, font='Verdana 20')
cpf_ent = Entry(cadastro_cliente, font='Verdana 20')
dataNasc_ent = Entry(cadastro_cliente, font='Verdana 20')
num_ent = Entry(cadastro_cliente, font='Verdana 20')

gravar = Button(cadastro_cliente, text='Cadastrar', font='Verdana 20', command=lambda: cadastrar_cliente())
voltar = Button(cadastro_cliente, text='Voltar', font='Verdana 20',
                command=lambda: [cadastro_cliente.pack_forget(), tela_login.pack(anchor='center', expand=1)])

num_conta = Label(tela_cliente, text='N° da Conta:', font='Verdana 20')
num_conta_ent = Entry(tela_cliente, font='Verdana 20')
conta_entrar = Button(tela_cliente, text='Entrar!', font='Verdana 20', command=entrar)

cliente_nome = Label(tela_cliente_dados, text='Nome:', font='Verdana 20')
cliente_cpf = Label(tela_cliente_dados, text='CPF:', font='Verdana 20')
cliente_dataNasc = Label(tela_cliente_dados, text='Data Nasc.:', font='Verdana 20')
cliente_num = Label(tela_cliente_dados, text='N° da conta:', font='Verdana 20')
cliente_saldo = Label(tela_cliente_dados, text='Saldo:', font='Verdana 20')

cliente_votar = Button(tela_cliente_menu, text='Sair', font='Verdana 20', width=10,
                       command=lambda: [tela_cliente_menu.grid_forget(),
                                        tela_cliente_dados.grid_forget(),
                                        tela_cliente_extrato.grid_forget(),
                                        tela_login.pack(anchor='center', expand=1)])
cliente_saque = Button(tela_cliente_menu, text='Saque', font='Verdana 20', width=10,
                       command=lambda: tela_cliente_saque.grid(row=2, column=0, columnspan=2))
cliente_deposito = Button(tela_cliente_menu, text='Deposito', font='Verdana 20', width=10,
                          command=lambda: tela_cliente_deposito.grid(row=2, column=0, columnspan=2))
cliente_transferencia = Button(tela_cliente_menu, text='Transferencia', font='Verdana 20', width=10,
                               command=lambda: tela_cliente_transferencia.grid(row=2, column=0, columnspan=2))
cliente_extrato = Button(tela_cliente_menu, text='Extrato', font='Verdana 20', width=10,
                         command=lambda: [cliente_imprimir_extrato(),
                                          extrato_saida.pack(fill=X)])

tela_login.pack(anchor='center', expand=1)

cliente.pack(anchor='center', padx=10)
funcionario.pack(anchor='center', pady=10)

nome.grid(row=0, column=0)
cpf.grid(row=1, column=0)
dataNasc.grid(row=2, column=0)
num.grid(row=3, column=0)

nome_ent.grid(row=0, column=1)
cpf_ent.grid(row=1, column=1)
dataNasc_ent.grid(row=2, column=1)
num_ent.grid(row=3, column=1)

gravar.grid(row=4, column=1)
voltar.grid(row=4, column=0)

num_conta.grid(row=0, column=0)
num_conta_ent.grid(row=0, column=1)
conta_entrar.grid(row=1, column=1)

cliente_nome.grid(row=0, column=0)
cliente_cpf.grid(row=1, column=0)
cliente_dataNasc.grid(row=2, column=0)
cliente_num.grid(row=3, column=0)
cliente_saldo.grid(row=4, column=0)

cliente_votar.pack()
cliente_saque.pack()
cliente_deposito.pack()
cliente_transferencia.pack()
cliente_extrato.pack()

tela_cliente_deposito = LabelFrame(root, text='deposito', font='Verdana 20')
valor_ent = Entry(tela_cliente_deposito, font='Verdana 20')
confirmar_deposito = Button(tela_cliente_deposito, text='Confirmar', font='Verdana 20', command=cliente_depositar)
valor_ent.grid(row=0, column=0)
confirmar_deposito.grid(row=0, column=1)

tela_cliente_saque = LabelFrame(root, text='saque', font='Verdana 20')
saque_ent = Entry(tela_cliente_saque, font='Verdana 20')
confirmar_saque = Button(tela_cliente_saque, text='Confirmar', font='Verdana 20', command=cliente_sacar)
saque_ent.grid(row=0, column=0)
confirmar_saque.grid(row=0, column=1)

tela_cliente_transferencia = LabelFrame(root, text='transferencia', font='Verdana 20')
transferencia_ent = Entry(tela_cliente_transferencia, font='Verdana 20')
transferencia_conta_ent = Entry(tela_cliente_transferencia, font='Verdana 20')
confirmar_transferencia = Button(tela_cliente_transferencia, text='Confirmar', font='Verdana 20',
                                 command=cliente_transferir)
transferencia_ent.grid(row=0, column=0)
transferencia_conta_ent.grid(row=1, column=0)
confirmar_transferencia.grid(row=0, column=1)

tela_cliente_extrato = LabelFrame(root, text='extrato', font='Verdana 20')
extrato_saida = Label(tela_cliente_extrato, font='Verdana 20')

root.mainloop()
