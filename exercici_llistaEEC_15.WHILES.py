#15 amb whiles - no surt

compt = 0
comptRBA = 0
q1 = input("Qualitat: ")

while compt<10:
    compt=compt+1
    q1 = input("Qualitat: ")
    if q1 == "R":
        compt=compt+1
        q2 = input("Qualitat: ")
        if q2 == "B":
            compt=compt+1
            q3 = input("Qualitat: ")
            if q3 == "A":
                compt=compt+1
                comptRBA=comptRBA+1
                q1= input("Qualitat: ")
print(comptRBA)


    
