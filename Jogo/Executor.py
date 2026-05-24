class Executor:
    def __init__(self, jogador):
        self.jogador = jogador
        self.fila_acoes = []
        self.acao_atual = None
        self.executando = False

    def carregar_acoes(self, acoes):
        self.fila_acoes = list(acoes)
        self.acao_atual = None
        self.executando = len(self.fila_acoes) > 0

        if self.executando:
            self._iniciar_proxima_acao()

    def executar_todas(self):
        while self.executando:
            self.atualizar()

    def atualizar(self):
        if not self.executando or self.acao_atual is None:
            return False

        self.jogador.x += self.jogador.vel_x
        self.jogador.y += self.jogador.vel_y

        terminou = self.acao_atual.atualizar(self)

        if terminou:
            self._iniciar_proxima_acao()

        return self.executando

    def _iniciar_proxima_acao(self):
        if len(self.fila_acoes) == 0:
            self.acao_atual = None
            self.executando = False
            return

        # pop(0) pega a primeira
        self.acao_atual = self.fila_acoes.pop(0)
        self.acao_atual.iniciar(self)
