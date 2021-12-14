# ExamenElBueno
Mi dirección de github es la siguiente:[Github](https://github.com/Barroso03/ExamenElBueno.git)

Hemos creado dos juegos:
# 1. The minion game
Kevin y Stuart quieren jugar al ' The Minion Game '.
Reglas del juego
Ambos jugadores reciben la misma cadena de caracteres
Ambos jugadores tienen que hacer subcadenas usando las letras de la cadena
Stuart tiene que formar palabras que comiencen con consonantes .
Kevin tiene que formar palabras que comiencen con vocales .
El juego termina cuando ambos jugadores han creado todas las subcadenas posibles.
Puntuación
Un jugador obtiene un +1punto por cada aparición de la subcadena en la cadena.
Por ejemplo :
String= BANANA
Palabra inicial de la vocal de Kevin = ANA
Aquí, ANA aparece dos veces en BANANA . Por lo tanto, Kevin obtendrá 2puntos.
Para una mejor comprensión, vea la imagen a continuación:

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

el código de las torres verticales es el siguiente:

