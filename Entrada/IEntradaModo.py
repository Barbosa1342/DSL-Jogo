import abc

class I_entrada_modo(abc.ABC):
    @abc.abstractmethod
    def ler_entrada(self):
        pass

class entrada_modo_arquivo(I_entrada_modo):
    def __init__(self, entrada):
        self.entrada = entrada
        self.indice = 0

    def ler_entrada(self):
        if (len(self.entrada) <= self.indice):
            return None

        comando = self.entrada[self.indice]

        self.indice += 1
        
        return comando
    
class entrada_modo_comando(I_entrada_modo):
    def __init__(self):
        pass
    
    def ler_entrada(self):
        comando = input("Digite um comando (ou 'sair' para encerrar): ")
        
        if comando.strip().lower() in ("sair", "exit", "quit"):
            print("Encerrando o jogo.")
            return None
        
        return comando