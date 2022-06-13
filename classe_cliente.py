class Cliente:

    def __init__(self, nome: str, cpf: str, dataNasc: str):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

    def imprime_dados(self):
        print(f'Nome: {self.nome}\ncpf: {self.cpf}\n'
              f'Data de Nasc: {self.dataNasc}')