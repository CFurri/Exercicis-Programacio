#15

comptadorRBA = 0
comptador30 = 0


while comptador30 < 10:
    q1 = input("Qualitat: ")
    comptador30 = comptador30 + 1
    if q1 == "R":
        comptador30 = comptador30 + 1
        q2 = input("Qualitat: ")
        if q2 == "B":
            comptador30 = comptador30 + 1
            q3 = input("Qualitat: ")
            if q3 == "A" :
                comptador30 = comptador30 + 1
                comptadorRBA = comptadorRBA + 1
   
            
print(comptadorRBA)
        
        
    
    
    
    


