from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._datanascimento = data_nascimento

    @property
    @abstractmethod
    def nome(self):
        return self._nome

    @property
    @abstractmethod
    def cpf(self):
        return self._cpf

    @property
    @abstractmethod
    def data_nascimento(self):
        return self._datanascimento
