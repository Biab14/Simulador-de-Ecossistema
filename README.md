# Simulador de Ecossistemas — Modelo Lotka-Volterra

Este projeto simula um ecossistema com presas (coelhos), predadores (raposas) e plantas, baseado nos conceitos do modelo de Lotka-Volterra.

A simulação inclui:
- Movimento aleatório
- Caça com raio de percepção
- Consumo de energia
- Morte e transferência de nutrientes ao solo
- Reprodução com base em energia
- Ciclo de plantas
- Espaço toroidal

## Estrutura do Projeto
- src/ — código principal
- models/ — classes de Coelho, Raposa, Planta, Ecossistema
- interface/ — menus e gráficos
- assets/ — imagens e sons
- docs/ — documentação do grupo

## Como rodar
python src/main.py

## Requisitos
As bibliotecas necessárias estão listadas em:
- requirements.txt

Para instalá-las:

pip install -r requirements.txt