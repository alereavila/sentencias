"""""
Objetivo: nombre y genero perteneces al un grupo
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)
"""

nombre=input("Introduce tu nombre:  ")
genero=input("Introduce tu genero:  ")

if not genero.upper() in ("M","F"):
    print("Genero no reconocido")
elif (genero.upper() == "F" and nombre[0].lower()<"m") or genero.upper()=="M" and nombre[0].lower()>"m":
    print("Pertenece G1")
else:
    print("Pertenece a G2")
