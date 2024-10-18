# una altra manera de fer-ho exercici 9

h = int(input("Digues una hora: "))
m = int(input("Digues els minuts: "))
s = int(input("Digues els segons: "))

s += 1 #per tallar el codi s == s + 1

if s == 60:
    m = m + 1
    s = 0
    if m == 60:
        h = h + 1
        m = 0
        if h == 24:
            h = 0
            
print(h)
print(m)
print(s)


