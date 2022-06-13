from classe_historico import Historico

class Conta:

    def __init__(self, objeto, num: str, saldo=0.0):
        self.titular = objeto.nome
        self.num = num
        self.saldo = saldo
        self.historico = Historico()

    def extrato(self):
        print(f'='*30,f'\nTitular: {self.titular}\nSaldo: {self.saldo}')
        self.historico.transacoes_bancarias()

    def deposito(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de {valor}')
        return self.saldo

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')
            return self.saldo
        else:
            print('Saldo insuficiente para o saque!')

    def transfere(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f'tranferencia de {valor} para a conta {destino.num}')
            return self.saldo
        else:
            print('Saldo insuficiente para o saque!')

    def transfere_para(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.recebe_transferencia(valor,self)
            self.historico.transacoes.append(f'tranferencia de {valor} para a conta {destino.num}')
            return self.saldo
        else:
            print('Saldo insuficiente para a transferencia!')

    def recebe_transferencia(self, valor, origem):
        self.saldo += valor
        self.historico.transacoes.append(f'tranferencia de {valor} da conta {origem.num}')