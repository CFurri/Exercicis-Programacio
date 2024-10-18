#17 DISSET!!!!!!

qualitat = input("Qualitat: ")
comptador = 0
qualitat_primer = qualitat

while qualitat != "*":
    qualitat = input("Qualitat: ")
    if qualitat_primer == qualitat:
        comptador = comptador + 1
    
print(comptador)
    

