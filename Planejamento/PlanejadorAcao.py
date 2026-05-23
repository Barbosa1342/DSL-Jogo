import Modelo.ItemAcao as ItemAcao

class PlanejadorAcao:
    def __init__(self, gerenciador_acoes):
        self.gerenciador_acoes = gerenciador_acoes

    def planejar_acao(self, ast):
        for acao in ast['acao']:
            acao_planejada = ItemAcao.ItemAcao(acao["tipo"], acao["acao"], acao["intensidade"])
            self.gerenciador_acoes.adicionar_acao(acao_planejada)
    
    def resetar_planejamento(self):
        self.gerenciador_acoes.resetar_acoes()
