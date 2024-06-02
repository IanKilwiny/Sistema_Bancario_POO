from cliente import Cliente
from historico import Historico
class Conta:

    def __init__(self,numero,cliente,saldo):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historio = Historico()
        self._contas  = []

        self._contas.append({
            "nome":cliente.nome,
            "numero":self._agencia+numero
        })
    
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
    
    @property
    def contas(self):
        return self._contas

     
    def criar_nova_conta(self):
        numero = int(self._numero)
        numero+=1
        self._contas.append({
            "nome":self._cliente.nome,
            "conta":self.agencia + str(numero)
        })
        print("Nova conta criada")
