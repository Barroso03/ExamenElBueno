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

        

