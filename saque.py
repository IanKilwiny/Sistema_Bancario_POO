from transacao import Transacao


class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor
        self._contador = 0

    @property
    def valor(self):
        return self._valor

    @property
    def contador(self):
        self._contador += 1
        return self._contador
