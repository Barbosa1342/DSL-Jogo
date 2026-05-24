import abc

class I_acao(abc.ABC):
    @abc.abstractmethod
    def iniciar(self, executor):
        pass

    def atualizar(self, executor):
        pass

    def finalizar(self, executor):
        pass
