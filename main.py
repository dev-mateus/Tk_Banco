from classe_cliente import *
from classe_conta import *

p1 = Cliente(nome='Mateus', cpf='12345678', dataNasc='06/05/1988')
c1 = Conta(p1, num='123-4')

p2 = Cliente(nome='Rodrigo', cpf='12345690', dataNasc='02/04/1987')
c2 = Conta(p2, num='123-6')

c1.deposito(500)
c1.transfere_para(50,c2)

c1.extrato()
c2.extrato()