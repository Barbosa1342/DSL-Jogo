from Codigo.Jogo.Acoes.IAcao import I_acao

class acao_coletar(I_acao):
    def __init__(self, num_slot):
        self.frames = 0
        self.duracao = 30
        self.num_slot = num_slot
        
    def iniciar(self, executor):
        executor.jogador.estado.atualizar_estado("Coletando")
        executor.jogador.inventario.adicionar_item(self.num_slot, "ItemColetado")

    def atualizar(self, executor):
        self.frames += 1

        if self.frames >= self.duracao:
            self.finalizar(executor)
            return True

        return False

    def finalizar(self, executor):
        executor.jogador.estado.atualizar_estado("Levantado")

