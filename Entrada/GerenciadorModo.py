class gerenciador_modo():
    def __init__(self):
        pass

    def set_modo(self):
        while True:
            modo = int(input("Escolha o modo de entrada (1 para arquivo, 2 para linha de comando): "))

            if (modo != 1) and (modo != 2):
                print("Modo inválido. Por favor, escolha 1 ou 2.")
                return self.set_modo()
            
            return modo
    
    def get_modo(self):
        return self.modo