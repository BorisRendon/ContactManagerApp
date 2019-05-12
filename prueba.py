import os.path,time,sys

"""""fase 1"""
contactos=[]
#------------------------------------------------------funcion agregar contactos--------------------------------------------------
def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)
#------------------------------------------------------funcion listar contactos--------------------------------------------------
def listar_contactos(contactos):   
    contador=0
    for k in (contactos):       
        print(" ---------------------------")
        print("|        contacto #{}       |".format(contador))
        print(" ---------------------------")
        for i,n in k.items(): 
            print("{}: {}".format(i,n))
        print ("contact id es {}".format(contador))
        contador = contador +1
agregar_contacto("fabricio","juarez","123")
#------------------------------------------------------funcion eliminar contactos--------------------------------------------------
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
#------------------------------------------------------funcion chequeo de archivo con impresion--------------------------------------------------
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
#------------------------------------------------------funcion agregar id a contactos--------------------------------------------------
def contact_id (contactos):
    contador = 0 
    contactos_cid={} 
    for i in contactos:
        contactos_cid[contador]=i
        contador = contador +1
#------------------------------------------------------funcion llamar contactos--------------------------------------------------
def call_id (contactos,id):
    conta=contactos[id]
    id_per=conta ["nombre"]
    id_num = conta ["numero"]
    print ("calling {}...".format(id_per))
    print("numero de telefono: {}".format(id_num))
    contador =5

    for i in range(5):
        time.sleep(1)
        print("Espere en linea {} segundos restantes".format(contador))
        contador =contador - 1

#------------------------------------------------------menu temporal--------------------------------------------------
menup = "si"
while menup == "si":
        print("")
        print("--------------------------------menu principal contact manager--------------------------------------------")
        print("")
        print("1. ajustes de contactos")
        print("2. comunicarse con algun contacto")
        print("10. exit ")
        print("")
        opcion_menu_prin = int(input("ingrese numero de opcion "))
        if opcion_menu_prin == 1 :               
                menuaj = "si"
                while menuaj =="si":
                        print("")
                        print("--------------------------------Ajustes de contactos--------------------------------------------")
                        print("")
                        print("1. agregar contactos")
                        print("2. listar contactos")
                        print("3. eliminar contactos")
                        print("")
                        opcion_ajustes = int(input("ingrese numero de opcion "))
                        print("")
                        if opcion_ajustes == 1:
                                nombre = input("Nombre:  ")
                                apellido = input("Apellido: ")
                                numero =input("Numero ")
                                agregar_contacto(nombre,apellido,numero)
                        if opcion_ajustes == 2:
                                listar_contactos(contactos)
                        if opcion_ajustes == 3:
                                nombre = input("Nombre ")   
                                eliminar_contactos (nombre)
                        menuaj = input("Desea realizar otra accion? ")
        if opcion_menu_prin == 2 :
                
                menucont = "si"
                while menucont == "si":
                        print("")
                        print("--------------------------------Ajustes de contactos--------------------------------------------")
                        print("")
                        print("1. llamar contacto ")
                        
                        print("")
                        opcion_cont = int(input("ingrese numero de opcion "))
                        print("")
                        if opcion_cont == 1:
                                id= int(input("Ingrese id a llamar "))
                                print("")
                                call_id(contactos,id)
                        print("")
                        menucont = input("Desea realizar otra accion? ")
        if opcion_menu_prin == 10 :
                print("gracias por utilizar contact manager")
                sys.exit()
        
   






