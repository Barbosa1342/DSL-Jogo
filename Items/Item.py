class Item:
    def __init__(self, nome, sprite, x, y):
        self.nome = nome
        self.sprite = sprite
        self.x = x
        self.y = y
        self.coletada = False

    def copiar(self):
        item = Item(self.nome, self.sprite, self.x, self.y)
        item.coletada = self.coletada
        return item
