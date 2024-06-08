import datetime 
class Historico:
    
    def __init__(self):
        self._transacao = []

    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor":transacao.valor,
                "hora":datetime.datetime.now().strftime("%H:%M:%S"),
                "data":datetime.datetime.now().strftime("%d/%m/%y")
            }
        )
        
    def historico_transacao(self):
        return self._transacao
