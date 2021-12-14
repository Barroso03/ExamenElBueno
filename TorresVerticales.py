import math
import os
import random
import re
import sys

def torrreVertical(r1, r2):
    comienza = 2
    for torre_1,torre_2 in zip(r1,r2):
        distancia = abs(torre_2-torre_1)
        ganador = ""
        if comienza == 2:
            if distancia == 1:
                ganador = "Jugador 1"
                comienza = 2
            else:
                ganador = "Jugador 2"
                comienza = 1
        else:
            if distancia == 1:
                ganador = "Jugador 2"
                comienza = 1
            else:
                ganador = "Jugador 1"
                comienza = 2
    
    if ganador == "Jugador 1":
        return "player-1"
    else:
        return "player-2" 
