from classe_cliente import *
from classe_conta import *
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
            print(clientes[i].nome, clientes[i].cpf, contas[i].num, contas[i].saldo)

            tela_cliente.pack_forget()
            tela_cliente_dados.pack()
            cliente_nome['text'] += clientes[i].nome
            cliente_cpf['text'] += clientes[i].cpf
            cliente_dataNasc['text'] += clientes[i].dataNasc
            cliente_num['text'] += contas[i].num


root = Tk()

tela_login = LabelFrame(root, text='Login')
cadastro_cliente = LabelFrame(root, text='Cadastro')
tela_cliente = LabelFrame(root, text='login')
tela_cliente_dados = LabelFrame(root, text='dados')

cliente = Button(tela_login, text='Cliente',  command=lambda: [tela_cliente.pack(), tela_login.pack_forget()])
funcionario = Button(tela_login, text='Funcionario', command=lambda: [cadastro_cliente.pack(), tela_login.pack_forget()])

nome = Label(cadastro_cliente, text='Nome: ')
cpf = Label(cadastro_cliente, text='CPF: ')
dataNasc = Label(cadastro_cliente, text='Data Nasc.: ')
num = Label(cadastro_cliente, text='N° da conta: ')

nome_ent = Entry(cadastro_cliente)
cpf_ent = Entry(cadastro_cliente)
dataNasc_ent = Entry(cadastro_cliente)
num_ent = Entry(cadastro_cliente)

gravar = Button(cadastro_cliente, text='Cadastrar', command=lambda: cadastrar_cliente())
voltar = Button(cadastro_cliente, text='Voltar', command=lambda: [cadastro_cliente.pack_forget(), tela_login.pack()])

num_conta = Label(tela_cliente, text='N° da Conta:')
num_conta_ent = Entry(tela_cliente)
conta_entrar = Button(tela_cliente, text='Entrar!', command=entrar)

cliente_nome = Label(tela_cliente_dados, text='Nome:')
cliente_cpf = Label(tela_cliente_dados, text='CPF:')
cliente_dataNasc = Label(tela_cliente_dados, text='Data Nasc.:')
cliente_num = Label(tela_cliente_dados, text='N° da conta:')

tela_login.pack()

cliente.pack(fill=X)
funcionario.pack(fill=X)

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

root.mainloop()
