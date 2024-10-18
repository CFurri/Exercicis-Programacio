#. Fer un programa que donat un valor de x retorni el valor f(x) per la funció:
 # x/x-2 si x < 2 
 # f(x) = x2-4 si 2 <= x <= 5 
 # 2x/x-5 si x > 5

x = int(input("Digues un valor: "))

if x < 2:
    x = x/(x-2)
    
elif x >= 2 and x<= 5:
    x = (x*2)-4
    
elif x > 5:
    x = (2 * x) / (x - 5)

print(" f(x) = " , x )

