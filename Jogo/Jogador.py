from Codigo.Jogo.Inventario import Inventario
from Codigo.Jogo.Estado import Estado

class Jogador:
    def __init__(self, inventario : Inventario, estado : Estado):
        self.inventario = inventario
        self.estado = estado
        self.x = 0
        self.y = 0

        self.vel_x = 0
        self.vel_y = 0

        self.no_chao = True
        