class Estado:
    def __init__(self):
        self.estado = "Levantado"
    
    def atualizar_estado(self, novo_estado):
        self.estado = novo_estado
    
    def obter_estado(self):
        return self.estado

    def resetar_estado(self):
        self.estado = "Levantado"