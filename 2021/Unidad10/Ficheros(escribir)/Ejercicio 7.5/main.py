from os import write


try:
    texto=open("texto.txt", "w")
    lista=["a","b","s"]
    for i in lista:
        texto.write(i+"\n")
        #texto.write(i)
    texto.close()

except:
    print("error")