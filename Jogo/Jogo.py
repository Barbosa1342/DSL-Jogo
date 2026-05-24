import os
import sys

CODIGO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJETO_DIR = os.path.dirname(CODIGO_DIR)
JOGO_DIR = os.path.dirname(os.path.abspath(__file__))

if CODIGO_DIR not in sys.path:
    sys.path.append(CODIGO_DIR)

if PROJETO_DIR not in sys.path:
    sys.path.append(PROJETO_DIR)

if JOGO_DIR not in sys.path:
    sys.path.append(JOGO_DIR)

from Codigo.Entrada.GerenciadorModo import gerenciador_modo
from Codigo.Entrada.IEntradaModo import entrada_modo_arquivo, entrada_modo_comando
from Codigo.Utilidade.entradaSaidaParser import JsonOutputParser, JsonResetFile, TextoInputParser

from Analisador.AnalisadorSintatico import analisador_sintatico
from Analisador.AnalisadorSemantico import analisador_semantico
from Analisador.ValidadorMovimento import validador_movimento
from Analisador.ValidadorInteracao import validador_interacao

from Codigo.Jogo.Estado import Estado
from Codigo.Jogo.Inventario import Inventario

from Planejamento.GerenciadorAcoes import gerenciador_acoes
from Planejamento.PlanejadorAcao import planejador_acao

from Executor import Executor
from Jogador import Jogador
from Acoes.AcaoAgachar import acao_agachar
from Acoes.AcaoAndar import acao_andar
from Acoes.AcaoColetar import acao_coletar
from Acoes.AcaoLevantar import acao_levantar
from Acoes.AcaoPular import acao_pular
from Acoes.AcaoSoltar import acao_soltar
from Acoes.AcaoUsar import acao_usar


class Jogo:
    def __init__(self):
        self.jogador = Jogador(Inventario(4), Estado())

        self.inventario_planejamento = Inventario(4)
        self.estado_planejamento = Estado()

        self.analisador_sintatico = analisador_sintatico()
        self.analisador_semantico = analisador_semantico(
            validador_movimento(),
            validador_interacao(),
            self.inventario_planejamento,
            self.estado_planejamento
        )

        self.gerenciador_acoes = gerenciador_acoes()
        self.planejador_acoes = planejador_acao(self.gerenciador_acoes)
        self.executor = Executor(self.jogador)

    def executar_comando(self, comando):
        if self.executor.executando:
            print("Aguarde a execucao das acoes terminar.")
            return False

        ast_valida = self.analisar_comando(comando)

        if not ast_valida:
            return False

        self.planejar_acao(ast_valida)
        self.executar_acoes()
        
        self._exibir_pose()
        return ast_valida

    def analisar_comando(self, comando):
        ast = self.analisador_sintatico.analisar(comando)

        if isinstance(ast, Exception):
            print(f"Erro sintatico ao analisar o comando: '{comando}'")
            return False

        # Antes de validar o comando, sincronizamos o estado do planejamento com o estado atual do jogador
        self.analisador_semantico.inventario_planejamento.copiar_inventario(self.jogador.inventario)
        self.analisador_semantico.estado_planejamento.copiar_estado(self.jogador.estado)

        ast_valida = self.analisador_semantico.analisar_prefixo_valido(ast)

        if isinstance(ast_valida, Exception):
            print(f"Erro semantico ao analisar o comando: '{comando}'")
            return False

        if len(ast_valida["acao"]) == 0:
            print("Nenhuma acao valida para executar.")
            return False
        
        return ast_valida

    def planejar_acao(self, ast):
        self.planejador_acoes.planejar_acao(ast)

    def executar_acoes(self):
        acoes_executaveis = self._criar_acoes_executaveis(self.gerenciador_acoes.get_acoes())
        self.executor.carregar_acoes(acoes_executaveis)
        self.executor.executar_todas()

    def _criar_acoes_executaveis(self, acoes_planejadas):
        acoes_executaveis = []

        for acao in acoes_planejadas:
            if acao.tipo == "movimento":
                acoes_executaveis.append(self._criar_movimento(acao))
            elif acao.tipo == "interacao":
                acoes_executaveis.append(self._criar_interacao(acao))
            else:
                raise Exception(f"Tipo de acao desconhecido: {acao.tipo}")

        return acoes_executaveis

    def _criar_movimento(self, acao):
        if acao.acao == "anda":
            return acao_andar(acao.adicional)
        if acao.acao == "pula":
            return acao_pular(acao.adicional)
        if acao.acao == "agacha":
            return acao_agachar()
        if acao.acao == "levanta":
            return acao_levantar()

        raise Exception(f"Movimento desconhecido: {acao.acao}")

    def _criar_interacao(self, acao):
        if acao.acao == "coleta":
            return acao_coletar(acao.adicional)
        if acao.acao == "solta":
            return acao_soltar(acao.adicional)
        if acao.acao == "usa":
            return acao_usar(acao.adicional)

        raise Exception(f"Interacao desconhecida: {acao.acao}")

    def _exibir_pose(self):
        print(f"Jogador: x={self.jogador.x}, y={self.jogador.y}, estado={self.jogador.estado.obter_estado()}")
        print(f"Inventario: {self.jogador.inventario.slots}")


if __name__ == "__main__":
    jogo = Jogo()
    ger_modo = gerenciador_modo()
    modo = ger_modo.set_modo()

    saidaParser = JsonOutputParser()
    path_saida = "Data/astResultado.json"
    JsonResetFile().resetar(path_saida)

    if modo == 1:
        entradaParser = TextoInputParser()
        entrada = entradaParser.ler_entrada("Data/entrada.txt")
        entrada_m_arquivo = entrada_modo_arquivo(entrada.splitlines())
        
        comando = entrada_m_arquivo.ler_entrada()

        while comando is not None:
            ast_valida = jogo.executar_comando(comando)

            if not ast_valida:
                print(f"Erro ao analisar o comando: '{comando}'")
                break

            saidaParser.salvar_saida(path_saida, ast_valida)
            comando = entrada_m_arquivo.ler_entrada()

        print("Encerrando o programa.")
    elif modo == 2:
        entrada_m_comando = entrada_modo_comando()
        while True:
            comando = entrada_m_comando.ler_entrada()

            if comando is None:
                print("Encerrando o programa.")
                break

            ast_valida = jogo.executar_comando(comando)

            if not ast_valida:
                print(f"Erro ao analisar o comando: '{comando}'")
                continue

            saidaParser.salvar_saida(path_saida, ast_valida)
  
