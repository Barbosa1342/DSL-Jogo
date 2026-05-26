from Jogo.Acoes.AcoesExecutaveis import criar_acoes_executaveis

from Planejamento.GerenciadorAcoes import gerenciador_acoes
from Planejamento.PlanejadorAcao import planejador_acao
from Analisador.AnalisadorComando import analisador_comando

class processador_comando:
    def __init__(self, gerenciador_itens):
        self.gerenciador_itens = gerenciador_itens
        self.planejador_acoes = planejador_acao(gerenciador_acoes())
        self.analisador_comando = analisador_comando(gerenciador_itens)

    def processar(self, comando, jogador):
        ast_valida = self.analisador_comando.analisar(comando, jogador)

        if not ast_valida:
            return False, []

        self.planejador_acoes.planejar_acao(ast_valida)
        acoes_executaveis = criar_acoes_executaveis(
            self.planejador_acoes.gerenciador_acoes.get_acoes(),
            self.gerenciador_itens
        )

        return ast_valida, acoes_executaveis

    
