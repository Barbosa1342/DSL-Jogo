class validador_movimento():
    def __init__(self):
        pass

    def validar_agachar(self, jogador):
        if (jogador.estado.obter_estado() == "Levantado"):
            jogador.estado.atualizar_estado("Agachado")
            return True
        else:
            raise Exception("Erro Semantico: Jogador ja esta agachado")

    def validar_levantar(self, jogador):
        if (jogador.estado.obter_estado() == "Agachado"):
            jogador.estado.atualizar_estado("Levantado")
            return True
        else:
            raise Exception("Erro Semantico: Jogador ja esta levantado")

    def validar_andar(self, jogador):
        if (jogador.estado.obter_estado() == "Levantado"):
            return True
        else:
            raise Exception("Erro Semantico: Jogador não pode andar estando agachado")

    def validar_pular(self, jogador):
        if (jogador.estado.obter_estado() == "Levantado"):
            return True
        else:
            raise Exception("Erro Semantico: Jogador não pode pular estando agachado")
        
    def validar_virar(self, jogador):
        if (jogador.estado.obter_estado() == "Levantado"):
            return True
        else:
            raise Exception("Erro Semantico: Jogador não pode virar estando agachado")
