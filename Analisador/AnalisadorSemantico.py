'''
Analise Semantica
- Usar um Slot Vazio
- Coletar para um slot preenchido
- Soltar de um slot Vazio

- Agachar e Agachar
- Levantar e Levantar
- Pular agachado
- Andar Agachado
'''

class analisador_semantico():
    def __init__(self, validador_movimento, validador_interacao, inventario_planejamento, estado_planejamento):
        self.validador_movimento = validador_movimento
        self.validador_interacao = validador_interacao
        self.inventario_planejamento = inventario_planejamento
        self.estado_planejamento = estado_planejamento

    def analisar(self, ast):
        is_valido = False

        for acao in ast['acao']:
            if (acao["tipo"] == "movimento"):
                if (acao["acao"] == "anda"):
                    is_valido = self.validador_movimento.validar_andar(self.estado_planejamento)
                elif (acao["acao"] == "pula"):
                    is_valido = self.validador_movimento.validar_pular(self.estado_planejamento)
                elif (acao["acao"] == "agacha"):
                    is_valido = self.validador_movimento.validar_agachar(self.estado_planejamento)
                elif (acao["acao"] == "levanta"):
                    is_valido = self.validador_movimento.validar_levantar(self.estado_planejamento)
            elif (acao["tipo"] == "interacao"):
                if (acao["acao"] == "coleta"):
                    is_valido = self.validador_interacao.validar_coletar(self.inventario_planejamento, acao["num_slot"])
                    if (is_valido):
                        self.inventario_planejamento.adicionar_item(acao["num_slot"], "ITEM COLETADO")

                elif (acao["acao"] == "solta"):
                    is_valido = self.validador_interacao.validar_soltar(self.inventario_planejamento, acao["num_slot"])
                    if (is_valido):
                        self.inventario_planejamento.remover_item(acao["num_slot"])

                elif (acao["acao"] == "usa"):
                    is_valido = self.validador_interacao.validar_usar(self.inventario_planejamento, acao["num_slot"])
            else:
                raise Exception("Erro Semantico: Tipo de acao desconhecido")
   
        return is_valido
    
    def resetar_analisador(self):
        self.inventario_planejamento.resetar_inventario()
        self.estado_planejamento.resetar_estado()