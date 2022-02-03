"""""
Objetivo: Sentencia de control
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)
Programa que muestra un Hola Mundo
"""
MAYORIA_EDAD=18
edad= int(input("Proporcopna tu edad:   "))
if edad<MAYORIA_EDAD:
    print("Eres menor de edad mijamon")
else:
    print("Eres mayor de edad")
print("Sentencia for")
rango=range(10)
print(rango)
for x in rango:
    print("El valor de x es {x}".format(x=x))

lista=["a","b","c","d","e"]
for caracter in lista:
    print("El caracter es {} de la lista".format(caracter))
tupla=(1,2,3,4)
for elemento in tupla:
    print("Imprime los valoes {}".format(elemento))
diccionario={"nombre":"carlos","edad":42,"tel":5239}

for llave in diccionario.keys():
    print("Valores en x : {}".format(diccionario[llave]))
