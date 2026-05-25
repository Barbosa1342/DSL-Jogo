import pygame
import os

def carregar_sprite(caminho, escala_jogador):
        # convert_alpha mantem a transparencia do png
        imagem = pygame.image.load(caminho).convert_alpha()
        largura, altura = imagem.get_size()

        if largura > altura:
            imagem = imagem.subsurface(pygame.Rect(0, 0, altura, altura)).copy()
            largura = altura

        tamanho = (largura * escala_jogador, altura * escala_jogador)
        return pygame.transform.scale(imagem, tamanho)

def carregar_sprites_jogador(caminho, escala_jogador):
        pasta_assets = caminho
        #os.path.join(CODIGO_DIR, "assets")

        return {
            "Levantado": carregar_sprite(os.path.join(pasta_assets, "playerParado.png"), escala_jogador),
            "Andando": carregar_sprite(os.path.join(pasta_assets, "playerAndando.png"), escala_jogador),
            "Pulando": carregar_sprite(os.path.join(pasta_assets, "playerPulando.png"), escala_jogador),
            "Agachado": carregar_sprite(os.path.join(pasta_assets, "playerAgachado.png"), escala_jogador),
            "Coletando": carregar_sprite(os.path.join(pasta_assets, "playerInteragir.png"), escala_jogador),
            "Soltando": carregar_sprite(os.path.join(pasta_assets, "playerInteragir.png"), escala_jogador),
            "Usando": carregar_sprite(os.path.join(pasta_assets, "playerInteragir.png"), escala_jogador),
            "Virando": carregar_sprite(os.path.join(pasta_assets, "playerParado.png"), escala_jogador),
        }

def carregar_sprites_item(caminho, escala_item):
        pasta_assets = caminho

        return {
            "Chave Prata": carregar_sprite(os.path.join(pasta_assets, "chavePrata.png"), escala_item),
            "Chave Dourada": carregar_sprite(os.path.join(pasta_assets, "chaveDourada.png"), escala_item),
        }