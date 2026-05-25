import abc
import pygame

class I_entrada_modo(abc.ABC):
    @abc.abstractmethod
    def ler_entrada(self):
        pass

class entrada_modo_arquivo(I_entrada_modo):
    def __init__(self, entrada):
        self.entrada = entrada
        self.indice = 0
        self.finalizado = False

    def ler_entrada(self):
        if (len(self.entrada) <= self.indice):
            self.finalizado = True
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
    
class entrada_modo_pygame(I_entrada_modo):
    def __init__(self):
        self.comando_digitado = ""
        self.finalizado = False

    def ler_entrada(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.finalizado = True
                return None

            if evento.type != pygame.KEYDOWN:
                continue

            if evento.key == pygame.K_ESCAPE:
                self.finalizado = True
                return None

            if evento.key == pygame.K_RETURN:
                comando = self.comando_digitado.strip()
                self.comando_digitado = ""

                if comando.lower() in ("sair", "exit", "quit"):
                    self.finalizado = True
                    return None

                return comando

            if evento.key == pygame.K_BACKSPACE:
                self.comando_digitado = self.comando_digitado[:-1]
            elif evento.unicode:
                self.comando_digitado += evento.unicode
