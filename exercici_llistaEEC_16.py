#16 #No entenc el perquè em carrego el primer input si el fico després del while
# L'error que cometo és ficar la variable dintre l'if. Aquesta ha d'anar regida pel while!
temps = float(input("Temperatura: "))
comptador = 0

while temps != 0:
    if temps > 0:
        comptador = comptador + 1
    temps = float(input("Temperatura: "))
if temps == 0:
    print(comptador)
        
    
