from Jogo.Inventario import Inventario
from Jogo.Estado import Estado

class Jogador:
    def __init__(self, inventario : Inventario, estado : Estado):
        self.inventario = inventario
        self.estado = estado
        self.x = 0
        self.y = 0

        self.vel_x = 0
        self.vel_y = 0

        self.no_chao = True
        self.virado_para_direita = True
        self.min_x = 0
        self.max_x = None
        self.raio_coleta = 32

    def direcao_horizontal(self):
        if self.virado_para_direita:
            return 1

        return -1

    def limitar_posicao_horizontal(self):
        if self.x < self.min_x:
            self.x = self.min_x

        if self.max_x is not None and self.x > self.max_x:
            self.x = self.max_x
        
