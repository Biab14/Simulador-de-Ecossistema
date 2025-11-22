from src.models.environment import Ecossistema
from src.models.animals import Coelho, Raposa
from src.models.plants import Planta
from src.simulation_loop import ciclo_simulacao
import random

def iniciar_simulacao():
    eco = Ecossistema()

    # populações iniciais
    for _ in range(20):
        eco.lista_coelhos.append(Coelho(random.randint(0, 9999),
                                        random.random()*500,
                                        random.random()*500))
    for _ in range(8):
        eco.lista_raposas.append(Raposa(random.randint(0, 9999),
                                        random.random()*500,
                                        random.random()*500))
    for _ in range(30):
        eco.lista_plantas.append(Planta(random.randint(0, 9999),
                                        random.random()*500,
                                        random.random()*500))

    for _ in range(1000):  # rodar 1000 ciclos
        ciclo_simulacao(eco)

    print("Fim da simulação!")
    print("Coelhos:", len(eco.lista_coelhos))
    print("Raposas:", len(eco.lista_raposas))
    print("Plantas:", len(eco.lista_plantas))

if __name__ == "__main__":
    iniciar_simulacao()