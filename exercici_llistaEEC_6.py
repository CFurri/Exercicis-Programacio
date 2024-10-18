#Fer un programa que donat un any ens digui si és bixest. És bixest si és divisible per 4 i no per 100 o bé per 400.


data = int(input("Digues un any: "))
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
           print("És bixest!")
else:
    print("No és bixest!")
           


                  
