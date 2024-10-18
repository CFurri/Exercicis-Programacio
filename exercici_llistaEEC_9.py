#Fer un programa que donada una hora, un minuts i uns segons, li sumi un segon i retorni el resultat en format horari correcte.

h = int(input("Digues una hora: "))
m = int(input("Digues els minuts: "))
s = int(input("Digues els segons: "))


if h == 23 and m == 59 and s == 59:
    (print("0 hores"))
    (print("0 minuts"))
    (print("0 segons"))

elif m == 59 and s == 59:
    h = h + 1
    m = 0
    s = 0
    print(h)
    print(m)
    print(s)

elif s == 59:
    m = m + 1
    s = 0
    print(h)
    print(m)
    print(s)
    
else:
    print(h)
    print(m)
    print(s + 1)


        
    


    



