from ply.lex import lex
from ply.yacc import yacc

'''
S ::= "Jogador" <Ação>
<Ação> ::=  <movimento> “e” <Ação> | <interacao> “e” <Ação> | <movimento> | <interacao>

<movimento> ::= “anda” <intensidade> | ”pula” <intensidade> | ”agacha”
<interacao> ::= “usa o” <slot> | ”coleta para”<slot> | ”solta do” <slot>

<intensidade> ::= “pouco” | ”muito”
<slot> ::= “1” | “2” | “3” | ”4”
'''

tokens = (
    "JOGADOR",

    "CMD_ANDAR",
    "CMD_PULAR",
    "CMD_AGACHAR",
    "CMD_LEVANTAR",

    "CMD_USAR",
    "CMD_COLETAR",
    "CMD_SOLTAR",

    "ARTIGO",
    "PREP_PARA",
    "PREP_DO",

    "SEQUENCIA",
    "INTENSIDADE",
    "NUM_SLOT"
    )

t_JOGADOR = r"\bJogador\b"

t_CMD_ANDAR = r"\banda\b"
t_CMD_PULAR = r"\bpula\b"
t_CMD_AGACHAR = r"\bagacha\b"
t_CMD_LEVANTAR = r"\blevanta\b"

t_CMD_USAR = r"\busa\b"
t_CMD_COLETAR = r"\bcoleta\b"
t_CMD_SOLTAR = r"\bsolta\b"

t_ARTIGO = r"\bo\b"
t_PREP_PARA = r"\bpara\b"
t_PREP_DO = r"\bdo\b"

t_SEQUENCIA = r"\be\b"
t_INTENSIDADE = r"\bpouco|muito\b"

t_NUM_SLOT = r"[1-4]"

t_ignore = " \t"

def t_error(t):
    print(f"Lexema Invalido: {t.value} na linha {t.lineno} e coluna {t.lexpos}")
    t.lexer.skip(1)
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# <comando> ::= JOGADOR <acao>
def p_comando(p):
    '''
    comando : JOGADOR acao
    '''

    p[0] = {
        "tipo": "comando",
        "acao": p[2]
    }

# <acao> :: = <movimento> e <Ação> | <interacao> e <Ação> | <movimento> | <interacao>
def p_acao(p):
    '''
    acao : movimento SEQUENCIA acao
         | interacao SEQUENCIA acao
         | movimento
         | interacao
    '''

    if (len(p) == 4):
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

# <movimento> ::= anda <intensidade> | pula <intensidade> | agacha | levanta
def p_movimento(p):
    '''
    movimento : CMD_ANDAR INTENSIDADE
              | CMD_PULAR INTENSIDADE
              | CMD_AGACHAR
              | CMD_LEVANTAR
    '''

    if (len(p) == 3):
        p[0] = {
            "tipo": "movimento",
            "acao": p[1],
            "intensidade": p[2]
        }
    else:
        p[0] = {
            "tipo": "movimento",
            "acao": p[1],
            "intensidade": ""
        }

# <interacao> ::= usa SLOT | coleta SLOT | solta SLOT
#                 | usa o SLOT | solta o SLOT
#                 | coleta para o SLOT | solta do SLOT
def p_interacao(p):
    '''
    interacao : CMD_USAR NUM_SLOT
              | CMD_COLETAR NUM_SLOT
              | CMD_SOLTAR NUM_SLOT
              | CMD_USAR ARTIGO NUM_SLOT
              | CMD_SOLTAR ARTIGO NUM_SLOT
              | CMD_COLETAR PREP_PARA ARTIGO NUM_SLOT
              | CMD_SOLTAR PREP_DO NUM_SLOT
    '''

    slot = int(p[len(p)-1])

    p[0] = {
            "tipo": "interacao",
            "acao": p[1],
            "num_slot": slot
        }
    

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno} e coluna {p.lexpos}, lexema {p.value} - tipo {p.type}")
    else:
        print("Erro de sintaxe: Comando Incompleto")

parser = yacc(write_tables=False)
lexer = lex()

class analisador_sintatico:
    def __init__(self):
        self.parser = parser
        self.lexer = lexer

    def analisar(self, comando):
        ast = self.parser.parse(comando)

        if ast is None:
            return Exception("Falha na analise sintatica")
        else:
            return ast