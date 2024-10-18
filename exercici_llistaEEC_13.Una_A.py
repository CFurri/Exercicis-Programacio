#13. una A

compt = 0
q = input("Qualitat: ")

while q != "A" and q != "*":
    compt = compt + 1
    q = input("Qualitat: ")
if q == "*":
    print("No hi ha cap A")
else:
    print(compt)
