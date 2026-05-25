from Codigo.Jogo.Acoes.AcaoAgachar import acao_agachar
from Codigo.Jogo.Acoes.AcaoAndar import acao_andar
from Codigo.Jogo.Acoes.AcaoColetar import acao_coletar
from Codigo.Jogo.Acoes.AcaoLevantar import acao_levantar
from Codigo.Jogo.Acoes.AcaoPular import acao_pular
from Codigo.Jogo.Acoes.AcaoSoltar import acao_soltar
from Codigo.Jogo.Acoes.AcaoUsar import acao_usar
from Codigo.Jogo.Acoes.AcaoVirar import acao_virar

def criar_acoes_executaveis(acoes_planejadas, gerenciador_itens):
    acoes_executaveis = []

    for acao in acoes_planejadas:
        if acao.tipo == "movimento":
            acoes_executaveis.append(criar_movimento(acao))
        elif acao.tipo == "interacao":
            acoes_executaveis.append(criar_interacao(acao, gerenciador_itens))
        else:
            raise Exception(f"Tipo de acao desconhecido: {acao.tipo}")

    return acoes_executaveis

def criar_movimento(acao):
    if acao.acao == "anda":
        return acao_andar(acao.adicional)
    if acao.acao == "pula":
        return acao_pular(acao.adicional)
    if acao.acao == "agacha":
        return acao_agachar()
    if acao.acao == "levanta":
        return acao_levantar()
    if acao.acao == "vira":
        return acao_virar()

    raise Exception(f"Movimento desconhecido: {acao.acao}")

def criar_interacao(acao, gerenciador_itens):
    if acao.acao == "coleta":
        item = gerenciador_itens.obter_item(acao.adicional["item_nome"])
        return acao_coletar(acao.adicional["num_slot"], item)
    if acao.acao == "solta":
        return acao_soltar(acao.adicional)
    if acao.acao == "usa":
        return acao_usar(acao.adicional)

    raise Exception(f"Interacao desconhecida: {acao.acao}")
