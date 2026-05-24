from Codigo.Planejamento.AcaoPlanejada import movimento_planejado, interacao_planejada

class planejador_acao:
    def __init__(self, gerenciador_acoes):
        self.gerenciador_acoes = gerenciador_acoes

    def planejar_acao(self, ast):
        self.resetar_planejamento()

        for acao in ast['acao']:
            if acao["tipo"] == "movimento":
                acao_plan = movimento_planejado(acao["acao"], acao["intensidade"])
            elif acao["tipo"] == "interacao":
                acao_plan = interacao_planejada(acao["acao"], acao["num_slot"])
            else:
                raise Exception(f"Tipo de ação desconhecido: {acao['tipo']}")

            self.gerenciador_acoes.adicionar_acao(acao_plan)
            print(f"Ação planejada: {acao_plan.tipo} - {acao_plan.acao} - Adicional: {acao_plan.adicional}")

    def resetar_planejamento(self):
        self.gerenciador_acoes.resetar_acoes()
