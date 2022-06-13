class Historico:

    def __init__(self):
        self.transacoes = []

    def transacoes_bancarias(self):
        print('Transações: ')
        for i in self.transacoes:
            print("-", i)