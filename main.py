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


def cadastrar():

    cliente = [Cliente(nome=nome_ent.get(), cpf=cpf_ent.get(), dataNasc=dataNasc_ent.get())]


def consultar():

    print(cliente)


root = Tk()
cadastro_cliente = LabelFrame(root, text='Cadastro Cliente')
cadastro_conta = LabelFrame(root, text='Cadastro Conta')

nome = Label(cadastro_cliente, text='Nome:')
cpf = Label(cadastro_cliente, text='CPF:')
dataNasc = Label(cadastro_cliente, text='Data Nasc.:')

nome_ent = Entry(cadastro_cliente)
cpf_ent = Entry(cadastro_cliente)
dataNasc_ent = Entry(cadastro_cliente)
cpf_consulta = Entry(cadastro_cliente)

gravar = Button(cadastro_cliente, text='Cadastrar', command=lambda: cadastrar())
listar = Button(cadastro_cliente, text='Consultar', command=lambda: consultar())

cadastro_cliente.pack()
nome.grid(row=0, column=0)
cpf.grid(row=1, column=0)
dataNasc.grid(row=2, column=0)

nome_ent.grid(row=0, column=1)
cpf_ent.grid(row=1, column=1)
dataNasc_ent.grid(row=2, column=1)
cpf_consulta.grid(row=4, column=1)

gravar.grid(row=3, column=1)
listar.grid(row=5, column=1)

root.mainloop()
