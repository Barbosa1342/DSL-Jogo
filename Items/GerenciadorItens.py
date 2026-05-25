from Codigo.Items.Item import Item

class gerenciador_itens:
    def __init__(self, inicializar=True):
        self.itens = {}
        if inicializar:
            self.inicializar_itens()

    def registrar_item(self, nome, item):
        self.itens[nome] = item

    def obter_item(self, nome):
        return self.itens.get(nome, None)

    def obter_itens_visiveis(self):
        return [item for item in self.itens.values() if not item.coletada]

    def copiar_de(self, gerenciador_origem):
        self.itens = {
            nome: item.copiar()
            for nome, item in gerenciador_origem.itens.items()
        }

    def copiar(self):
        novo_gerenciador = gerenciador_itens(inicializar=False)
        novo_gerenciador.copiar_de(self)
        return novo_gerenciador

    def inicializar_itens(self):
        self.registrar_item("Chave Prata", Item("Chave Prata", "Chave Prata", 90, 0))
        self.registrar_item("Chave Dourada", Item("Chave Dourada", "Chave Dourada", 360, 0))
