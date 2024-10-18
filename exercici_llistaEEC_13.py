#13. amb dues A - no surt

compt = 0
q_ant = ""
q = input("Qualitat: ")
    
while not((q == "A" and q_ant == "A") or (q == "*")):
    compt = compt + 1
    q_ant = q 
    q = input("Qualitat: ")
print(compt)
    
    
    
    


       
        

        
    




    
    
