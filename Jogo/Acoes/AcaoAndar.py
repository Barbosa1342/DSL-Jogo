from Jogo.Acoes.IAcao import I_acao

class acao_andar(I_acao):
    def __init__(self, intensidade):
        self.velocidade = 3
        self.frames = 0

        if intensidade == "pouco":
            self.duracao = 30
        elif intensidade == "muito":
            self.duracao = 60

    def iniciar(self, executor):
        executor.jogador.estado.atualizar_estado("Andando")
        executor.jogador.vel_x = self.velocidade * executor.jogador.direcao_horizontal()
        executor.jogador.vel_y = 0
    
    def atualizar(self, executor):
        self.frames += 1

        if self.frames >= self.duracao:
            self.finalizar(executor)
            return True
        
        return False
    
    def finalizar(self, executor):
        executor.jogador.estado.atualizar_estado("Levantado")
        executor.jogador.vel_x = 0
        executor.jogador.vel_y = 0
