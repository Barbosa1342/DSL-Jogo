from Codigo.Jogo.Acoes.IAcao import I_acao

class acao_pular(I_acao):
    def __init__(self, intensidade):
        self.velocidade = 3
        self.frames = 0

        if intensidade == "pouco":
            self.duracao = 45
        elif intensidade == "muito":
            self.duracao = 90

    def iniciar(self, executor):
        executor.jogador.estado.atualizar_estado("Pulando")
        executor.jogador.vel_x = 0
        executor.jogador.vel_y = self.velocidade
    
    def atualizar(self, executor):
        self.frames += 1

        if self.frames > int(self.duracao / 2):
            executor.jogador.vel_y = -self.velocidade

        if self.frames >= self.duracao:
            self.finalizar(executor)
            return True
        
        return False
    
    def finalizar(self, executor):
        executor.jogador.estado.atualizar_estado("Levantado")
        executor.jogador.vel_x = 0
        executor.jogador.vel_y = 0
