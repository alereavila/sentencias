"""""
Objetivo: 3 numeros cual es el mayor
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)
Programa que muestra un Hola Mundo
"""
numero1=int(input("Introduce un numero  "))
numero2=int(input("Introduce un numero  "))
numero3=int(input("Introduce un numero  "))

if numero1>numero2 and numero1>numero3:
    print("el numero 1 {num1} es el mayor".format(num1=numero1))
elif numero2>numero3:
    print("el numero 2 {num2} es el mayor".format(num2=numero2))
else:
    print("el numero 3 {num3} es el mayor".format(num3=numero3))