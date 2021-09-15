while True:
    try:
        palabra=input("Ingrese una palabra:")
        if palabra.isalpha():
            for i in palabra:
                print(i)
            break
        else:
            print("No ingreso una palabra")
    except:
        print("Error")