class analisador_comando():
    def __init__(self, analisador_sintatico, analisador_semantico):
        self.analisador_sintatico = analisador_sintatico
        self.analisador_semantico = analisador_semantico
        
    def analisar(self, comando):
        try:
            ast = self.analisador_sintatico.analisar(comando)

            if isinstance(ast, Exception):
                print(f"Erro sintatico no comando '{comando}': {ast}")
                raise Exception(f"Erro sintatico no comando '{comando}': {ast}")

            is_valido = self.analisador_semantico.analisar(ast)

            if isinstance(is_valido, Exception):
                print(f"Erro semantico no comando '{comando}': {is_valido}")
                raise Exception(f"Erro semantico no comando '{comando}': {is_valido}")

            print("Comando analisado com sucesso!")
            return ast           
        except Exception as e:
            print(f"{str(e)}")
            return None
