from random import uniform
from src.config import *

class Animal:
    def __init__(self, id, x, y, energia, velocidade):
        self.id = id
        self.x = x
        self.y = y
        self.energia = energia
        self.velocidade = velocidade
        self.idade = 0

    def mover(self):
        # Movimento aleatório básico
        self.x += uniform(-self.velocidade, self.velocidade)
        self.y += uniform(-self.velocidade, self.velocidade)

        # Espaço toroidal (teletransporte nas bordas)
        self.x %= LARGURA_MAPA
        self.y %= ALTURA_MAPA

        self.energia -= CUSTO_MOVIMENTO

    def gastar_energia(self):
        self.energia -= CUSTO_EXISTENCIA
        self.idade += 1


class Coelho(Animal):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, ENERGIA_INICIAL_COELHO, velocidade=4)
        self.energia_min_reproducao = 50
        self.ultimo_alimento = -1

    def comer(self, planta):
        self.energia += planta.energia
        self.ultimo_alimento = self.idade

    def pode_reproduzir(self):
        return self.energia >= self.energia_min_reproducao


class Raposa(Animal):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, ENERGIA_INICIAL_RAPOSA, velocidade=5)
        self.raio_percepcao = 50
        self.energia_min_reproducao = 70
        self.ultimo_coelho_comido = -1

    def comer(self, coelho):
        self.energia += coelho.energia
        self.ultimo_coelho_comido = self.idade

    def pode_reproduzir(self):
        return self.energia >= self.energia_min_reproducao