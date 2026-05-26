from Analisador.AnalisadorSintatico import analisador_sintatico
from Analisador.AnalisadorSemantico import analisador_semantico

class analisador_comando():
    def __init__(self, gerenciador_itens):
        self.analisador_sintatico = analisador_sintatico()
        self.analisador_semantico = analisador_semantico(gerenciador_itens)
        
    def analisar(self, comando, jogador):
        ast = self.analisador_sintatico.analisar(comando)

        if isinstance(ast, Exception):
            print(f"Erro sintatico ao analisar o comando: '{comando}'")
            return False

        self.analisador_semantico.preparar_planejamento(jogador)

        ast_valida = self.analisador_semantico.analisar_parcial_valido(ast)

        if isinstance(ast_valida, Exception):
            print(f"Erro semantico ao analisar o comando: '{comando}'")
            return False

        if len(ast_valida["acao"]) == 0:
            print("Nenhuma acao valida para executar.")
            return False

        return ast_valida
