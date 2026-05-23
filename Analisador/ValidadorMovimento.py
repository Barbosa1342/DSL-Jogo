class validador_movimento():
    def __init__(self):
        pass

    def validar_agachar(self, estado):
        if (estado.obter_estado() == "Levantado"):
            estado.atualizar_estado("Agachado")
            return True
        else:
            raise Exception("Erro Semantico: Jogador ja esta agachado")

    def validar_levantar(self, estado):
        if (estado.obter_estado() == "Agachado"):
            estado.atualizar_estado("Levantado")
            return True
        else:
            raise Exception("Erro Semantico: Jogador ja esta levantado")

    def validar_andar(self, estado):
        if (estado.obter_estado() == "Levantado"):
            return True
        else:
            raise Exception("Erro Semantico: Jogador não pode andar estando agachado")

    def validar_pular(self, estado):
        if (estado.obter_estado() == "Levantado"):
            return True
        else:
            raise Exception("Erro Semantico: Jogador não pode pular estando agachado")
