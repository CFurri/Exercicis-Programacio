#19

llindar = float(input("Llindar: "))
comptador_mitjana = 0
sobre_llindar = 0

while not comptador_mitjana == 5:
    mitjana = float(input("Mitjana durant 30 dies: "))
    comptador_mitjana = comptador_mitjana + 1
    if mitjana > llindar:
        sobre_llindar = sobre_llindar + 1
print(sobre_llindar)


