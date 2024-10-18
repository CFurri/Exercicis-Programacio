#7. Fer un programa que ens retorni el valor absolut d’un número.
numero = float(input("Digues un número: "))
print(abs(numero))

#una altra opció ( i més legal)

numero = float(input("Digues un número: "))
if numero >= 0:
    print(numero)
elif numero < 0:
    print(numero * -1)



