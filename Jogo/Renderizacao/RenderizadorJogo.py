import pygame

from Jogo.Renderizacao.ProcessaSprite import carregar_sprites_item, carregar_sprites_jogador

class renderizador_jogo:
    def __init__(self, caminho_assets, largura=800, altura=480, escala_jogador=4):
        self.largura_tela = largura
        self.altura_tela = altura
        self.chao_y = 360
        self.comando_digitado = ""

        pygame.display.set_caption("DSL Plataforma")
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        self.fonte = pygame.font.Font(None, 28)
        self.sprites_jogador = carregar_sprites_jogador(caminho_assets, escala_jogador)
        self.sprites_item = carregar_sprites_item(caminho_assets, escala_jogador)
        self.margem_jogador = 80

    def atualizar_comando(self, comando):
        self.comando_digitado = comando

    def processar_eventos_janela(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

        return True

    def desenhar(self, jogador, itens=None):
        self.tela.fill((132, 190, 214))
        pygame.draw.rect(self.tela, (86, 143, 90), (0, self.chao_y, self.largura_tela, self.altura_tela - self.chao_y))
        pygame.draw.line(self.tela, (58, 98, 63), (0, self.chao_y), (self.largura_tela, self.chao_y), 4)

        self.desenhar_item(itens or [])

        sprite = self.sprite_atual_jogador(jogador)
        sprite = self.aplicar_direcao_jogador(jogador, sprite)
        x_tela = self.posicao_x_jogador(jogador, sprite)
        y_tela = self.posicao_y_jogador(jogador, sprite)
        self.tela.blit(sprite, (x_tela, y_tela))

        self.desenhar_entrada(jogador)
        pygame.display.flip()

    def desenhar_item(self, itens):
        for item in itens:
            if item.coletada:
                continue

            sprite = self.sprites_item.get(item.sprite)

            if sprite is None:
                continue

            x_tela = self.margem_jogador + item.x
            y_tela = self.chao_y - sprite.get_height() - item.y
            self.tela.blit(sprite, (x_tela, y_tela))

    def sprite_atual_jogador(self, jogador):
        estado_atual = jogador.estado.obter_estado()
        return self.sprites_jogador.get(estado_atual, self.sprites_jogador["Levantado"])

    def aplicar_direcao_jogador(self, jogador, sprite):
        if jogador.virado_para_direita:
            return sprite

        return pygame.transform.flip(sprite, True, False)

    def posicao_x_jogador(self, jogador, sprite):
        largura_sprite = sprite.get_width()
        margem = self.margem_jogador
        x_tela = margem + jogador.x

        # limite minimo
        if x_tela < margem:
            return margem

        # limite maximo
        if x_tela > self.largura_tela - largura_sprite - margem:
            return self.largura_tela - largura_sprite - margem

        return x_tela

    def limite_x_jogador(self):
        sprite = self.sprites_jogador["Levantado"]
        return self.largura_tela - sprite.get_width() - (self.margem_jogador * 2)

    def posicao_y_jogador(self, jogador, sprite):
        estado_atual = jogador.estado.obter_estado()
        deslocamento_pulo = min(jogador.y, 96) if estado_atual == "Pulando" else 0
        return self.chao_y - sprite.get_height() - deslocamento_pulo

    def desenhar_entrada(self, jogador):
        altura_barra = 72
        y_barra = self.altura_tela - altura_barra
        pygame.draw.rect(self.tela, (26, 31, 36), (0, y_barra, self.largura_tela, altura_barra))
        pygame.draw.line(self.tela, (62, 70, 77), (0, y_barra), (self.largura_tela, y_barra), 2)

        texto_comando = self.fonte.render("> " + self.comando_digitado, True, (238, 241, 243))
        self.tela.blit(texto_comando, (24, y_barra + 24))

        texto_estado = self.fonte.render(jogador.estado.obter_estado(), True, (180, 206, 220))
        self.tela.blit(texto_estado, (self.largura_tela - texto_estado.get_width() - 24, y_barra + 24))
