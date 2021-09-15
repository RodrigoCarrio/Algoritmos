flag = True
while flag:
    try:
        dato_numerico=int(input("Ingrese un numero:"))
        flag = False
    except:
        print("Error")
        
multiplicador=1
while multiplicador<=10:
    print(f"{multiplicador}x{dato_numerico}= {multiplicador*dato_numerico}") 
    multipplicador+=1