import math
import os
import random
import re
import sys

def torreVertical(r1, r2):
    comienza = 2
    for torre_1, torre_2 in zip(r1,r2):
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
        return "Jugador 1"
    else:
        return "Jugador 2"




if __name__ == '__main__':
    

    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())

        r1 = []

        for _ in range(n):
            posicion_torre_1 = int(input().strip())
            r1.append(posicion_torre_1)

        r2 = []

        for _ in range(n):
            posicion_torre_2 = int(input().strip())
            r2.append(posicion_torre_2)

        result = torreVertical(r1, r2)

        print.write(result + '\ n') 
