class Planta:
    def __init__(self, id, x, y, energia=15):
        self.id = id
        self.x = x
        self.y = y
        self.energia = energia
        self.idade = 0
        self.ciclos_para_reproduzir = 8