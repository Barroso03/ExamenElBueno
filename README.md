# ExamenElBueno
Mi dirección de github es la siguiente:[Github](https://github.com/Barroso03/ExamenElBueno.git)

Hemos creado dos juegos:
# 1. The minion game
Kevin y Stuart quieren jugar al ' The Minion Game '.
-Reglas del juego:

Ambos jugadores reciben la misma cadena de caracteres
Ambos jugadores tienen que hacer subcadenas usando las letras de la cadena
Stuart tiene que formar palabras que comiencen con consonantes .
Kevin tiene que formar palabras que comiencen con vocales .
El juego termina cuando ambos jugadores han creado todas las subcadenas posibles.

-Puntuación
Un jugador obtiene un +1punto por cada aparición de la subcadena en la cadena.

-Por ejemplo :
String= BANANA
Palabra inicial de la vocal de Kevin = ANA
Aquí, ANA aparece dos veces en BANANA . Por lo tanto, Kevin obtendrá 2puntos.

-Para una mejor comprensión, vea la imagen a continuación:

![image](https://user-images.githubusercontent.com/91721590/145983220-ed964380-60d2-4081-baad-cc83db2a18c5.png)

El código del juego del minion es:
```
# Definimos la función del juego minion
def minion_game(s):
    puntuacionStuart=0
    puntuacionKevin=0
    vocales= 'AEIOU'
    s=s.upper()
    for i in range(len(s)):
        if s[i] not in vocales:
            puntuacionStuart=puntuacionStuart+(len(s)-i)
        else:
            puntuacionKevin=puntuacionKevin+(len(s)-i)
    if puntuacionStuart>puntuacionKevin:
        print("Stuart ha ganado, puntuación:", puntuacionStuart)
    elif puntuacionStuart<puntuacionKevin:
        print("Kevin ha ganado, puntuación:", puntuacionKevin)
    else:
        print("Empate")

if __name__=='__main__':
    palabra= input("Elige una palabra: ")
    minion_game(palabra)
# FIN
```
# 2. Torrevertical
 HackerChess es una variante del ajedrez que se juega en la UAX. Es un juego que se juega entre 
dos jugadores que realizan movimientos por turnos hasta que uno de ellos no puede realizar 
ningún movimiento. El jugador que no puede hacer un movimiento pierde el juego y el otro 
jugador es declarado ganador. El juego se juega en un tablero con filas N y N columnas.
Las únicas piezas que se utilizan en el juego son las torres. Una torre en HackerChess se mueve 
solo verticalmente, lo que significa que nunca deja una columna a la que pertenece. Además, 
en un solo movimiento, una torre atraviesa cualquier número de casillas desocupadas.
Tenga en cuenta que no hay capturas en HackerChess, dos torres no pueden ocupar la misma 
celda y una torre no puede saltar sobre otra torre. Cada jugador tiene exactamente una torre 
en cada una de las columnas del tablero.
Dada la posición inicial de las torres y sabiendo que el segundo jugador hace el primer 
movimiento, decide quién ganará el juego si ambos jugadores juegan de manera óptima.

-Formato de entrada:
En la primera línea, hay un solo entero T que denota el número de juegos a jugar. Después de 
eso, descripciones de T los juegos siguen:
En la primera línea, hay un solo entero N que denota el tamaño del tablero. Después siguen las 
N líneas.
En el i-th de ellos hay un solo entero r1i que denota la fila de la torre que pertenece al primer 
jugador colocado en la i-ésima columna. Después de eso, otro siguen las n líneas.
En el i-th de ellos hay un solo entero r2i que denota la fila de la torre que pertenece al segundo 
jugador colocado en el i-ésima columna.

-Restricciones:

![image](https://user-images.githubusercontent.com/91721590/145987460-7b0391a6-2b03-409c-9ae8-35f711732460.png)

-Formato de salida:
Imprimir exactamente t-líneas. En eli -th de ellos, imprima player-1si el primer jugador gana eli-ésimo juego. De lo contrario, imprima player-2en esta línea.

-Expliación 0:
Solo hay un jugador en la entrada de muestra. El juego se juega en el tablero con filas 
y columnas. Denotemos las torres del primer jugador como torres rojas y las torres del 
segundo jugador como torres verdes. Entonces, la posición inicial del juego se ve así:

![image](https://user-images.githubusercontent.com/91721590/145987951-b2556f12-2613-4379-b085-869a9c1b9270.png)

El segundo jugador se mueve primero y puede mover su torre en la primera columna a la 
segunda fila. Después de este movimiento, la posición se ve de la siguiente manera:

![image](https://user-images.githubusercontent.com/91721590/145988132-5bdb5777-adf6-42a4-a114-e15e27e1f1a8.png)

A continuación, es el turno del primer jugador. No puede hacer ningún movimiento con su 
torre en la primera columna, por lo que tiene que hacer un movimiento en la segunda o 
tercera columna. Sin perder la generalidad, supongamos que hace un movimiento en la 
segunda columna. Solo puede hacer uno de esos movimientos, es decir, mover la torre de la 
segunda a la tercera fila. Esto da como resultado la siguiente posición:

![image](https://user-images.githubusercontent.com/91721590/145988350-4ed879c4-5bd9-46e8-8650-700577ab25b2.png)

Después de eso, la mejor jugada para el segundo jugador es mover su torre en la segunda 
columna de la primera a la segunda fila. Después de este movimiento, la posición se ve así:

![image](https://user-images.githubusercontent.com/91721590/145988555-58340015-7e38-4996-97c4-e7d56f70f415.png)

Después de eso, la mejor jugada para el segundo jugador es mover su torre en la segunda 
columna de la primera a la segunda fila. Después de este movimiento, la posición se ve así:

![image](https://user-images.githubusercontent.com/91721590/145988697-b6ba7ca1-03cc-49fb-be57-5ce055eab45e.png)

A continuación, es nuevamente la jugada del primer jugador. El único movimiento que puede 
hacer es mover su torre en la tercera columna de la segunda a la tercera fila. Da como 
resultado la siguiente posición:

![image](https://user-images.githubusercontent.com/91721590/145988850-2592db90-a4ab-46d7-8fcf-2e0594389307.png)

Entonces, la mejor jugada para el segundo jugador es mover su torre en la tercera columna de 
la primera a la segunda fila. Después de eso, la posición se ve de la siguiente manera:

![image](https://user-images.githubusercontent.com/91721590/145988964-e09f4e4d-1484-4f56-8fc3-851c12939854.png)

A continuación, es la jugada del primer jugador, pero como no puede realizar ninguna jugada 
válida, pierde y el segundo jugador es declarado ganador.
Muestra que independientemente de los movimientos del primer jugador, el segundo jugador 
tiene una estrategia que lo lleva a la victoria.



El código de las torres verticales es el siguiente:
```
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

        print.write(result + '\ n'
```

