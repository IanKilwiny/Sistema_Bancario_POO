from conta import Conta
from saque import Saque
from deposito import Deposito
class ContaCorrente(Conta):

    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)
        self._limite = 0
        self._num_saques = 0
       
    
    def sacar(self, valor: float) -> str:
        LIMITE_VALOR = 500
        LIMITE_SAQUES = 3
        if valor <= self.saldo and self._num_saques < LIMITE_SAQUES and valor < LIMITE_VALOR:
            historico_saque = Saque(valor)
            self._historio.adicionar_transacao(historico_saque)
            self._num_saques+=1
            self._saldo-=valor
            return "Saque realizado com sucesso"
        elif valor>self.saldo:
            return "Valor acima do saldo"
        elif valor > LIMITE_VALOR:
            return "Ultrapassou o limite do valor de saque"
        elif self._num_saques >= LIMITE_SAQUES:
            return "Passou do limite de saques"

        
    
    def depositar(self, valor: float) -> bool:
        hist_deposito = Deposito(valor)
        historico = self._historio.adicionar_transacao(hist_deposito)
        self._saldo +=valor
    
    
    def __str__(self):
        return f"""
        ############# CONTA ##############
            Usuário:{self.cliente.nome}
            Conta:{self.agencia+str(self.numero)}
            Saldo:{self.saldo}
        ##################################
        """