from Utilidade.entradaSaidaParser import TextoInputParser, JsonOutputParser, JsonResetFile
from GerenciaExecucao.IEntradaModo import entrada_modo_arquivo, entrada_modo_comando
from GerenciaExecucao.gerenciadorModo import gerenciador_modo

from Analisador.AnalisadorSintatico import analisador_sintatico
from Analisador.AnalisadorSemantico import analisador_semantico
from Analisador.ValidadorMovimento import validador_movimento
from Analisador.ValidadorInteracao import validador_interacao
from Analisador.AnalisadorComando import analisador_comando

from Modelo.Inventario import Inventario
from Modelo.Estado import Estado

if __name__ == "__main__":
    path_saida = "Data/astResultado.json"

    JsonResetFile().resetar(path_saida)

    saidaParser = JsonOutputParser()
    

    val_movimento = validador_movimento()
    val_interacao = validador_interacao()
    inventario_planejamento = Inventario(4)
    estado_planejamento = Estado()

    anali_sintatico = analisador_sintatico()
    anali_semantico = analisador_semantico(val_movimento, val_interacao, inventario_planejamento, estado_planejamento)
    anali_comando = analisador_comando(anali_sintatico, anali_semantico)

    ger_modo = gerenciador_modo()
    modo = ger_modo.set_modo()

    if modo == 1:
        entradaParser = TextoInputParser()
        entrada = entradaParser.ler_entrada("Data/entrada.txt")
        entrada_m_arquivo = entrada_modo_arquivo(entrada.splitlines())

        
        comando = entrada_m_arquivo.ler_entrada()

        while comando is not None:
            ast = anali_comando.analisar(comando)
            
            if (ast is None):
                print(f"Erro ao analisar o comando: '{comando}'")
                break

            saidaParser.salvar_saida(path_saida, ast)

            comando = entrada_m_arquivo.ler_entrada()
        
        print("Encerrando o programa.")
    elif modo == 2:
        entrada_m_comando = entrada_modo_comando()
        while True:
            comando = entrada_m_comando.ler_entrada()

            if comando is None:
                print("Encerrando o programa.")
                break
            
            ast = anali_comando.analisar(comando)

            if (ast is None):
                print(f"Erro ao analisar o comando: '{comando}'")
                anali_semantico.resetar_analisador()
                continue
            
            saidaParser.salvar_saida(path_saida, ast)