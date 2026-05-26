import os

from Analisador.AnalisadorSintatico import analisador_sintatico
from Entrada.IEntradaModo import entrada_modo_arquivo
from Utilidade.entradaSaidaParser import TextoInputParser

CODIGO_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    analisador = analisador_sintatico()

    entradas = {
        1 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintaticoBasico.txt"),
        2 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintatico2.txt"),
        3 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintatico3.txt"),
        4 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintatico4.txt"),
        5 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintatico5.txt"),
        6 : os.path.join(CODIGO_DIR, "Data", "Teste Sintatico", "testeSintaticoFalha.txt")
    }

    resultados = {}

    entradaParser = TextoInputParser()

    for i in range(1, 7):
        falhas = 0
        sucessos = 0

        comandos = entradaParser.ler_entrada(entradas.get(i))
        entrada_m_arquivo = entrada_modo_arquivo(comandos.splitlines())

        while True:
            comando = entrada_m_arquivo.ler_entrada()

            if (comando is None):
                break

            resultado = analisador.analisar(comando)

            if isinstance(resultado, Exception):
                falhas += 1
            else:
                sucessos += 1

        resultados[i] = (sucessos, falhas)

    for i in range(1, 7):
        res = resultados.get(i)
        print(f"Resultado {i}. Sucessos: {res[0]}, Falhas: {res[1]}")
