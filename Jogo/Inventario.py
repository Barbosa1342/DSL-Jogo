class Inventario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.slots = [None] * tamanho

    def _indice_slot(self, num_slot):
        return num_slot - 1

    def is_slot_vazio(self, num_slot):
        # nao deve ocorrer devido a analise sintatica
        if num_slot < 1 or num_slot > self.tamanho:
            raise Exception(f"Numero do slot {num_slot} esta fora do limite do inventario")
        
        return self.slots[self._indice_slot(num_slot)] is None

    def adicionar_item(self, num_slot, item):
        if self.is_slot_vazio(num_slot):
            self.slots[self._indice_slot(num_slot)] = item
        else:
            raise Exception(f"Slot {num_slot} esta ocupado")

    def remover_item(self, num_slot):
        if not self.is_slot_vazio(num_slot):
            self.slots[self._indice_slot(num_slot)] = None
        else:
            raise Exception(f"Slot {num_slot} esta vazio")

    def obter_item(self, num_slot):
        if self.is_slot_vazio(num_slot):
            raise Exception(f"Slot {num_slot} esta vazio")

        return self.slots[self._indice_slot(num_slot)]
        
    def resetar_inventario(self):
        self.slots = [None] * self.tamanho

    def copiar_inventario(self, inventario_origem):
        if self.tamanho != inventario_origem.tamanho:
            raise Exception("Tamanhos de inventario sao diferentes")

        self.slots = list(inventario_origem.slots)