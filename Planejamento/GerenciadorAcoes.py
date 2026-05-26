from Planejamento.AcaoPlanejada import acao_planejada

class gerenciador_acoes:
    def __init__(self):
        self.acoes = []
    
    def adicionar_acao(self, tipo, acao, adicional):
        nova_acao = acao_planejada(tipo, acao, adicional)
        self.acoes.append(nova_acao)

    def adicionar_acao(self, acao):
        self.acoes.append(acao)

    def get_acoes(self):
        return self.acoes

    def resetar_acoes(self):
        self.acoes.clear()
