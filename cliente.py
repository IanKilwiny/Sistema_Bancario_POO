from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self,nome,cpf,data_nascimento, endereco):
        self._nome = nome
        self._cpf = cpf
        self._datanascimento = data_nascimento
        self._endereco = endereco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._datanascimento
    
    @property
    def endereco(self):
        return self._endereco
    
    def adicionar_conta(self,conta):
        
        pass

