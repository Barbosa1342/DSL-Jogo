inventario = {
    1 : "",
    2 : "",
    3 : "",
    4 : ""
}

# Usado para controlar o estado atual do jogador, animações e movimentação
# Possiveis: Agachado, Levantado, Andando, Pulando
# Jogador sempre termina a execucao Levantado ou Agachado
estado_controle = "Levantado"

def andar():
    # usar Pygame
    pass

def pular():
    # usar Pygame
    pass

def agachar():
    # usar Pygame
    pass

def levantar():
    # usar Pygame
    pass

def coletar_para(num_slot):
    # usar Pygame
    item = "DEVERIA SER UM ITEM NO MAPA"
    inventario[num_slot] = item
    pass

def soltar_do(num_slot):
    # usar Pygame
    inventario[num_slot] = ""
    pass

def usar_do(num_slot):
    # usar Pygame
    item = inventario.get(num_slot)
    print(f"Usado {item}")
    pass

def resetar_jogo():
    global inventario, estado_controle

    inventario = {
        1 : "",
        2 : "",
        3 : "",
        4 : ""
    }
    estado_controle = "Levantado"