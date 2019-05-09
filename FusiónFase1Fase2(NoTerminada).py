import os.path



"""""fase 1"""
contactos=[{"nombre":"fabricio","apellido":"perez","numero":"44"},{"nombre":"andres","apellido":"alvarado","numero":"46"}]

def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)
    print (contactos)

def listar_contactos(contactos):   
    contador=1
    for k in (contactos):       
        print(" ---------------------------")
        print("|        contacto #{}       |".format(contador))
        print(" ---------------------------")
        for i,n in k.items(): 
            print("{}: {}".format(i,n))
        contador = contador +1
listar_contactos(contactos)        
def eliminar_contactos (nombre):
    nombre_lista= nombre.split(" ")
    nombre_cliente= nombre_lista[0]
    apellido_cliente = nombre_lista[1]
    conta = 0
    for i in contactos:
        if i["nombre"]==nombre_cliente:
            if i["apellido"] == apellido_cliente:
                eliminar = contactos[conta]
                contactos.remove(eliminar)
        conta = conta +1
    print(contactos)





"""Fase 2"""

listavacia = []
diccionario ={}

def ChequeoArchivoExistenteConImpresion ():
    global contactos
    global listavacia
    global diccionario
    if(os.path.isfile("InitialContactList.txt")):
        f = open("InitialContactList.txt", "r") 
        print("El archivo si existe")
        with open("InitialContactList.txt") as f:
            for linea in f:
                (key,val) = linea.split()
                contactos[int(key)] = val
        print(contactos)
        
        
    else:
        print("No existe el archivo ")


ChequeoArchivoExistenteConImpresion()

        

        

        
