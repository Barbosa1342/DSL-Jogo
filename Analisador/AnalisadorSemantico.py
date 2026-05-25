from Codigo.Analisador.ValidadorInteracao import validador_interacao
from Codigo.Analisador.ValidadorMovimento import validador_movimento
from Codigo.Items.GerenciadorItens import gerenciador_itens
from Codigo.Jogo.Estado import Estado
from Codigo.Jogo.Inventario import Inventario
from Codigo.Jogo.Jogador import Jogador


class analisador_semantico():
    def __init__(self, gerenciador_itens_mundo=None):
        self.validador_movimento = validador_movimento()
        self.validador_interacao = validador_interacao()
        self.gerenciador_itens_mundo = gerenciador_itens_mundo or gerenciador_itens()
        self.gerenciador_itens_planejamento = self.gerenciador_itens_mundo.copiar()
        self.jogador_planejamento = Jogador(Inventario(4), Estado())

    def preparar_planejamento(self, jogador):
        self.jogador_planejamento.inventario.copiar_inventario(jogador.inventario)
        self.jogador_planejamento.estado.copiar_estado(jogador.estado)
        self.jogador_planejamento.x = jogador.x
        self.jogador_planejamento.y = jogador.y
        self.jogador_planejamento.virado_para_direita = jogador.virado_para_direita
        self.jogador_planejamento.min_x = jogador.min_x
        self.jogador_planejamento.max_x = jogador.max_x
        self.jogador_planejamento.raio_coleta = jogador.raio_coleta
        self.gerenciador_itens_planejamento.copiar_de(self.gerenciador_itens_mundo)

    def analisar(self, ast):
        for acao in ast['acao']:
            self.validar_acao(acao)

        return True

    def analisar_parcial_valido(self, ast):
        acoes_validas = []

        for acao in ast['acao']:
            try:
                self.validar_acao(acao)
                acoes_validas.append(acao)
            except Exception as erro:
                print(f"{str(erro)}")
                break

        return {
            "tipo": ast["tipo"],
            "acao": acoes_validas
        }

    def validar_acao(self, acao):
        if (acao["tipo"] == "movimento"):
            return self.validar_movimento(acao)

        if (acao["tipo"] == "interacao"):
            return self.validar_interacao(acao)

        raise Exception("Erro Semantico: Tipo de acao desconhecido")

    def validar_movimento(self, acao):
        if (acao["acao"] == "anda"):
            is_valido = self.validador_movimento.validar_andar(self.jogador_planejamento)
            self.simular_andar(acao["intensidade"])
            return is_valido
        elif (acao["acao"] == "pula"):
            return self.validador_movimento.validar_pular(self.jogador_planejamento)
        elif (acao["acao"] == "agacha"):
            return self.validador_movimento.validar_agachar(self.jogador_planejamento)
        elif (acao["acao"] == "levanta"):
            return self.validador_movimento.validar_levantar(self.jogador_planejamento)
        elif(acao["acao"] == "vira"):
            is_valido = self.validador_movimento.validar_virar(self.jogador_planejamento)
            self.jogador_planejamento.virado_para_direita = not self.jogador_planejamento.virado_para_direita
            return is_valido

        raise Exception("Erro Semantico: Movimento desconhecido")

    def validar_interacao(self, acao):
        if (acao["acao"] == "coleta"):
            is_valido, item_nome = self.validador_interacao.validar_coletar(
                self.gerenciador_itens_planejamento,
                self.jogador_planejamento,
                acao["num_slot"]
            )
            if (is_valido):
                acao["item_nome"] = item_nome
                self.jogador_planejamento.inventario.adicionar_item(acao["num_slot"], item_nome)
                self.gerenciador_itens_planejamento.obter_item(item_nome).coletada = True
            return is_valido

        elif (acao["acao"] == "solta"):
            is_valido = self.validador_interacao.validar_soltar(self.jogador_planejamento, acao["num_slot"])
            
            if (is_valido):
                item_nome = self.jogador_planejamento.inventario.obter_item(acao["num_slot"])
                item = self.gerenciador_itens_planejamento.obter_item(item_nome)
                
                if item is not None:
                    item.coletada = False
                    item.x = self.jogador_planejamento.x
                    item.y = self.jogador_planejamento.y
                    
                self.jogador_planejamento.inventario.remover_item(acao["num_slot"])
            
            return is_valido

        elif (acao["acao"] == "usa"):
            return self.validador_interacao.validar_usar(self.jogador_planejamento, acao["num_slot"])

        raise Exception("Erro Semantico: Interacao desconhecida")

    def simular_andar(self, intensidade):
        # baseado em AcaoAndar
        # velocidade * duracao
        # se mudar la, mudar aqui

        distancia = 90
        if intensidade == "muito":
            distancia = 180

        self.jogador_planejamento.x += distancia * self.jogador_planejamento.direcao_horizontal()
        self.jogador_planejamento.limitar_posicao_horizontal()
