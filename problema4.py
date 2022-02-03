series=int(input("Proporcione el numero de series"))
datos={}
for _ in range(series):
    nombre=input("Nombre de la serie")
    fcc=int(input("Frecuencia"))
    datos[nombre]=fcc

for n in datos.keys():
    print(n)
    print("x"*datos[n])
