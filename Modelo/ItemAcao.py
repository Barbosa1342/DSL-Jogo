class ItemAcao():
    def __init__(self, tipo, acao, adicional):
        self.tipo = tipo
        self.acao = acao
        self.adicional = adicional

class Movimento(ItemAcao):
    def __init__(self, movimento, intensidade):
        super().__init__("movimento", movimento, intensidade)

class Interacao(ItemAcao):
    def __init__(self, interacao, num_slot):
        super().__init__("interacao", interacao, num_slot)