import os
import sys
import pygame

JOGO_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.dirname(JOGO_DIR)

if PROJETO_DIR not in sys.path:
    sys.path.insert(0, PROJETO_DIR)

from Entrada.GerenciadorModo import gerenciador_modo
from Entrada.IEntradaModo import entrada_modo_arquivo, entrada_modo_pygame
from Utilidade.entradaSaidaParser import JsonOutputParser, JsonResetFile, TextoInputParser

from Items.GerenciadorItens import gerenciador_itens
from Items.Item import Item

from Jogo.Estado import Estado
from Jogo.Executor import Executor
from Jogo.Inventario import Inventario
from Jogo.Jogador import Jogador
from Jogo.Acoes.ProcessadorComando import processador_comando
from Jogo.Renderizacao.RenderizadorJogo import renderizador_jogo


class jogo:
    def __init__(self, entrada):
        self.entrada = entrada
        self.fps = 60
        self.rodando = True

        pygame.init()
        self.relogio = pygame.time.Clock()

        self.jogador = Jogador(Inventario(4), Estado())
        self.executor = Executor(self.jogador)
        self.renderizador = renderizador_jogo(os.path.join(PROJETO_DIR, "assets"))
        self.jogador.max_x = self.renderizador.limite_x_jogador()
        self.gerenciador_itens = gerenciador_itens()
        self.processador_comando = processador_comando(self.gerenciador_itens)

        self.desenhar()

    def executar_comando(self, comando):
        if not self.rodando:
            return False

        if self.executor.executando:
            print("Aguarde a execucao das acoes terminar.")
            return False

        self.processar_eventos_janela()
        self.renderizador.atualizar_comando(comando)
        self.desenhar()

        ast_valida, acoes_executaveis = self.processador_comando.processar(comando, self.jogador)

        if not ast_valida:
            return False

        self.executar_acoes(acoes_executaveis)
        self.exibir_pose()
        return ast_valida

    def executar_acoes(self, acoes_executaveis):
        self.executor.carregar_acoes(acoes_executaveis)

        while self.executor.executando and self.rodando:
            self.processar_eventos_janela()
            self.executor.atualizar()
            self.desenhar()
            self.relogio.tick(self.fps)

    def ler_comando(self):
        while self.rodando:
            comando = self.entrada.ler_entrada()
            texto_digitado = getattr(self.entrada, "comando_digitado", None)

            if texto_digitado is not None:
                self.renderizador.atualizar_comando(texto_digitado)

            if comando is not None:
                self.renderizador.atualizar_comando(comando)
                self.desenhar()
                return comando

            if getattr(self.entrada, "finalizado", False):
                self.rodando = False
                return None

            self.desenhar()
            self.relogio.tick(self.fps)

        return None

    def desenhar(self):
        self.renderizador.desenhar(self.jogador, self.gerenciador_itens.obter_itens_visiveis())

    def encerrar(self):
        pygame.quit()

    def processar_eventos_janela(self):
        self.rodando = self.renderizador.processar_eventos_janela()

    def exibir_pose(self):
        print(f"Jogador: x={self.jogador.x}, y={self.jogador.y}, estado={self.jogador.estado.obter_estado()}")

        print(f"Inventario: ")

        for item in self.jogador.inventario.slots:
            if item is not None:
                print(item.nome)


if __name__ == "__main__":
    ger_modo = gerenciador_modo()
    modo = ger_modo.set_modo()

    saidaParser = JsonOutputParser()
    path_saida = os.path.join(PROJETO_DIR, "Data", "astResultado.json")
    JsonResetFile().resetar(path_saida)

    if modo == 1:
        entradaParser = TextoInputParser()
        entrada = entradaParser.ler_entrada(os.path.join(PROJETO_DIR, "Data", "Teste Semantico", "testeSemanticoAnda.txt"))
        entrada_m_arquivo = entrada_modo_arquivo(entrada.splitlines())

        jogo = jogo(entrada_m_arquivo)
    elif modo == 2:
        entrada_m_pygame = entrada_modo_pygame()

        jogo = jogo(entrada_m_pygame)

    while jogo.rodando:
        comando = jogo.ler_comando()

        if comando is None:
            print("Encerrando o programa.")
            break

        ast_valida = jogo.executar_comando(comando)

        if not ast_valida:
            print(f"Erro ao analisar o comando: '{comando}'")
            continue

        saidaParser.salvar_saida(path_saida, ast_valida)

    jogo.encerrar()
