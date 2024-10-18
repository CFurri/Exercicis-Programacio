#Fer un programa que donats 3 valors numèrics d’entrada mostri quin és el més gran.

n1 = int(input("Escriu un valor: "))
n2 = int(input("Escriu un valor: "))
n3 = int(input("Escriu un valor: "))

if n1 > n2 and n1 > n3:
    print(n1)
elif n1 < n2 and n2 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)

