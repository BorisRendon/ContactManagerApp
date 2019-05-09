import os.path


"""Fase 2"""

listavacia = []
diccionario ={}

def ChequeoArchivoExistenteConImpresion ():
    global listavacia
    global diccionario
    if(os.path.isfile("InitialContactList.txt")):
        f = open("InitialContactList.txt", "r") 
        print("El archivo si existe")
        with open("InitialContactList.txt") as f:
            for linea in f:
                (key,val) = linea.split()
                diccionario[int(key)] = val
        print(diccionario)
        
        
    else:
        print("No existe el archivo ")



#with open("InitialContactList.txt") as f:
    #for linea in f:
     #   (key,val) = linea.split()
      #  diccionario[int(key)] = val


#print (diccionario)

ChequeoArchivoExistenteConImpresion()
#ith open('InitialContactList.txt', 'r') as f:
            #listavacia = [line.strip() for line in f]
    
        #print(listavacia)
        #for x in listavacia:
            #print(x.split(","))




