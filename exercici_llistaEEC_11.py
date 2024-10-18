# Fer un programa que donada una seqüència d’anys acabada en 0 ens digui quants n’hi ha del segle 20
añs = int(input("Digues un any: "))
inici = 0

while añs != 0:
    if añs >= 1901 and añs <= 2000:
        inici = inici + 1
    añs = int(input("Escribe otro año: "))
print(inici)
    
        
