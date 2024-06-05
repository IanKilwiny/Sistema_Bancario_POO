from cliente import Cliente
from historico import Historico
class Conta:

    def __init__(self,numero,cliente,saldo):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historio = Historico()

    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico_transacao(self):
        return self._historio.historico_transacao()
   
    @property
    def endereco(self):
        return self._endereco
   
