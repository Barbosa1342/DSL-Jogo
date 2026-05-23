class validador_interacao():
    def validar_coletar(self, inventario, num_slot):
        if(inventario.is_slot_vazio(num_slot)):
            return True
        else:
            raise Exception(f"Erro Semantico: Slot {num_slot} esta ocupado")

    def validar_soltar(self, inventario, num_slot):
        if(inventario.is_slot_vazio(num_slot)):
            raise Exception(f"Erro Semantico: Slot {num_slot} esta vazio")
        else:
            return True

    def validar_usar(self, inventario, num_slot):
        if(inventario.is_slot_vazio(num_slot)):
            raise Exception(f"Erro Semantico: Slot {num_slot} esta vazio")
        else:
            return True
