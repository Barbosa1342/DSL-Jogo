from Utilidade.calculaDistancia import calcula_distancia

class validador_interacao():
    def validar_coletar(self, gerenciador_itens, jogador, num_slot):
        if(jogador.inventario.is_slot_vazio(num_slot)):
            for item in gerenciador_itens.itens.values():
                if item.coletada:
                    continue

                if (calcula_distancia(jogador.x, jogador.y, item.x, item.y) <= jogador.raio_coleta):
                    return True, item.nome
            raise Exception("Erro Semantico: Jogador não esta proximo de nenhum item")
        else:
            raise Exception(f"Erro Semantico: Slot {num_slot} esta ocupado")

    def validar_soltar(self, jogador, num_slot):
        if(jogador.inventario.is_slot_vazio(num_slot)):
            raise Exception(f"Erro Semantico: Slot {num_slot} esta vazio")
        else:
            return True

    def validar_usar(self, jogador, num_slot):
        if(jogador.inventario.is_slot_vazio(num_slot)):
            raise Exception(f"Erro Semantico: Slot {num_slot} esta vazio")
        else:
            return True
