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
        for acao in ast['acao']:
            self.validar_acao(acao)
   
        return True

    def analisar_prefixo_valido(self, ast):
        acoes_validas = []

        for acao in ast['acao']:
            try:
                self.validar_acao(acao)
                acoes_validas.append(acao)
            except Exception as erro:
                print(f"{str(erro)}")
                break

        return {
            "tipo": ast["tipo"],
            "acao": acoes_validas
        }

    def validar_acao(self, acao):
        if (acao["tipo"] == "movimento"):
            if (acao["acao"] == "anda"):
                return self.validador_movimento.validar_andar(self.estado_planejamento)
            elif (acao["acao"] == "pula"):
                return self.validador_movimento.validar_pular(self.estado_planejamento)
            elif (acao["acao"] == "agacha"):
                return self.validador_movimento.validar_agachar(self.estado_planejamento)
            elif (acao["acao"] == "levanta"):
                return self.validador_movimento.validar_levantar(self.estado_planejamento)
        elif (acao["tipo"] == "interacao"):
            if (acao["acao"] == "coleta"):
                is_valido = self.validador_interacao.validar_coletar(self.inventario_planejamento, acao["num_slot"])
                if (is_valido):
                    self.inventario_planejamento.adicionar_item(acao["num_slot"], "ITEM COLETADO")
                return is_valido

            elif (acao["acao"] == "solta"):
                is_valido = self.validador_interacao.validar_soltar(self.inventario_planejamento, acao["num_slot"])
                if (is_valido):
                    self.inventario_planejamento.remover_item(acao["num_slot"])
                return is_valido

            elif (acao["acao"] == "usa"):
                return self.validador_interacao.validar_usar(self.inventario_planejamento, acao["num_slot"])

        raise Exception("Erro Semantico: Tipo de acao desconhecido")
    
    def resetar_analisador(self):
        self.inventario_planejamento.resetar_inventario()
        self.estado_planejamento.resetar_estado()
