from transacao import Transacao
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    # def registrar(self, conta):
    #     sucesso_transacao = conta.

    #     if sucesso_transacao:
    #         self._conta.adicionar_transacacao(self)
            