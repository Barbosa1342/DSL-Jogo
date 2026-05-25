from Codigo.Jogo.Acoes.IAcao import I_acao

class acao_virar(I_acao):
    def __init__(self):
        self.duracao = 30
        self.frames = 0

    def iniciar(self, executor):
        executor.jogador.virado_para_direita = not executor.jogador.virado_para_direita
        executor.jogador.estado.atualizar_estado("Virando")
    
    def atualizar(self, executor):
        self.frames += 1

        if self.frames >= self.duracao:
            self.finalizar(executor)
            return True
        
        return False
    
    def finalizar(self, executor):
        executor.jogador.estado.atualizar_estado("Levantado")
