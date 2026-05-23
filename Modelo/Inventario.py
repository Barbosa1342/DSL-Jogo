class Inventario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.slots = [None] * tamanho

    def is_slot_vazio(self, num_slot):
        # nao deve ocorrer devido a analise sintatica
        if num_slot < 1 or num_slot > self.tamanho:
            raise Exception(f"Numero do slot {num_slot} esta fora do limite do inventario")
        
        return self.slots[num_slot] is None

    def adicionar_item(self, num_slot, item):
        if self.is_slot_vazio(num_slot):
            self.slots[num_slot] = item
        else:
            raise Exception(f"Slot {num_slot} esta ocupado")

    def remover_item(self, num_slot):
        if not self.is_slot_vazio(num_slot):
            self.slots[num_slot] = None
        else:
            raise Exception(f"Slot {num_slot} esta vazio")
        
    def resetar_inventario(self):
        self.slots = [None] * self.tamanho