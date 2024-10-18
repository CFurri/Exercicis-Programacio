qualitat = input("Qualitat: ")
comptador = 0
while qualitat != "*":
    if qualitat == "R":
        comptador = comptador + 1
    qualitat = input("Qualitat: ")
print(comptador)

