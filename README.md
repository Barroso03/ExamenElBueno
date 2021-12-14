# ExamenElBueno
Mi dirección de github es la siguiente:[Github](https://github.com/Barroso03/ExamenElBueno.git)

Hemos creado el juego del minion que consiste en que sale la palabra banana o una parte de esa palabra y hay dos jugadores que son Kevin y Stuart, cada uno tiene su puntuación a Kevin le cuenta más las vocales y a Stuart las consonantes, gana el que tiene más puntuación.

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
