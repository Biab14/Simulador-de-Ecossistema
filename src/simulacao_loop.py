from src.models.animals import Coelho, Raposa
from src.models.plants import Planta
from src.models.environment import Ecossistema
from src.config import *
from random import randint, uniform
import math

def distancia(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def ciclo_simulacao(ecossistema: Ecossistema):
    # 1) Movimento
    for coelho in ecossistema.lista_coelhos:
        coelho.mover()

    for raposa in ecossistema.lista_raposas:
        raposa.mover()

    # 2) Coelhos comem plantas
    for coelho in ecossistema.lista_coelhos:
        for planta in ecossistema.lista_plantas:
            if distancia(coelho, planta) < 5:
                coelho.comer(planta)
                ecossistema.lista_plantas.remove(planta)
                break

    # 3) Raposas caçam coelhos
    for raposa in ecossistema.lista_raposas:
        coelhos_proximos = [c for c in ecossistema.lista_coelhos
                            if distancia(raposa, c) < raposa.raio_percepcao]

        if coelhos_proximos:
            alvo = min(coelhos_proximos, key=lambda c: distancia(raposa, c))
            raposa.comer(alvo)
            ecossistema.lista_coelhos.remove(alvo)

    # 4) Gastar energia / morte
    def processar_morte(lista, ecossistema):
        mortos = []
        for animal in lista:
            animal.gastar_energia()
            if animal.energia <= 0:
                mortos.append(animal)

        for m in mortos:
            lista.remove(m)
            ecossistema.nutrientes_solo += 5  # devolve nutrientes

    processar_morte(ecossistema.lista_coelhos, ecossistema)
    processar_morte(ecossistema.lista_raposas, ecossistema)

    # 5) Reprodução
    novos_coelhos = []
    for coelho in ecossistema.lista_coelhos:
        if coelho.pode_reproduzir():
            if randint(0, 20) == 1:  # 5% chance
                novos_coelhos.append(Coelho(randint(0, 99999),
                                            coelho.x + uniform(-3, 3),
                                            coelho.y + uniform(-3, 3)))
                coelho.energia *= 0.5

    ecossistema.lista_coelhos.extend(novos_coelhos)

    novos_predadores = []
    for raposa in ecossistema.lista_raposas:
        if raposa.pode_reproduzir():
            if randint(0, 20) == 1:  # 5%
                novos_predadores.append(Raposa(randint(0, 99999),
                                               raposa.x + uniform(-3, 3),
                                               raposa.y + uniform(-3, 3)))
                raposa.energia *= 0.5

    ecossistema.lista_raposas.extend(novos_predadores)

    # 6) Crescimento de plantas
    if ecossistema.ciclo_atual % CICLOS_PARA_NOVA_PLANTA == 0:
        if ecossistema.nutrientes_solo >= NUTRIENTES_MINIMOS:
            ecossistema.lista_plantas.append(
                Planta(randint(0, 99999),
                       uniform(0, LARGURA_MAPA),
                       uniform(0, ALTURA_MAPA))
            )
            ecossistema.nutrientes_solo -= 5

    # 7) Atualizar históricos
    ecossistema.historico_coelhos.append(len(ecossistema.lista_coelhos))
    ecossistema.historico_raposas.append(len(ecossistema.lista_raposas))
    ecossistema.historico_plantas.append(len(ecossistema.lista_plantas))

    # Incrementar ciclo
    ecossistema.ciclo_atual += 1