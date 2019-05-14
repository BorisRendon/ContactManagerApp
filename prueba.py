import os.path



def MenuPrincipal ():
    gt= "si"
    opcion = int(input("seleccione opcion\n(1)agregar\n(2)Listar contactos\n(3)eliminar Contacto\n"))
    
    if gt =="si":
        
        if opcion == 1:
            nombre = input("nombre ")
            apellido = input("apellido ")
            numero =input("numero ")
            agregar_contacto(nombre,apellido,numero)
        if opcion == 2:
            listar_contactos(contactos)
        if opcion == 3:
            nombre = input("nombre ")
            
            eliminar_contactos (nombre)
            
        gt = input("Desea agregar,listar o elimnar un contacto?\n")
    else:
        print("Saliendo...")


"""""fase 1"""
contactos=[]

def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)


def listar_contactos(contactos):   
    contador=1
    for k in (contactos):       
        print(" ---------------------------")
        print("|        contacto #{}       |".format(contador))
        print(" ---------------------------")
        for i,n in k.items(): 
            print("{}: {}".format(i,n))
        contador = contador +1
#agregar_contacto("fabricio","juarez","123")


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
    

"""Fase 2"""

listavacia = []
diccionario ={}

def ChequeoArchivoExistenteConImpresion (nombre,apellido,numero):
    global contactos
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
        print("No existe el archivo en el que desea trabajar ")




MenuPrincipal()
ChequeoArchivoExistenteConImpresion()



