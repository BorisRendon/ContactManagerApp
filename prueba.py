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
# gt= "si"
# print("")
# print("--------------------------------menu principal contact manager--------------------------------------------")
# print("")
# print("1.  agregar un contacto")
# print("2.  listar contactos")
# print("3.  eliminar un contacto")
# print("4.  llamar un contacto")
# print("")
# while gt =="si":
#     opcion = int(input("ingrese numero de opcion "))
#     print("")
#     if opcion == 1:
#         nombre = input("Nombre:  ")
#         apellido = input("Apellido: ")
#         numero =input("Numero ")
#         agregar_contacto(nombre,apellido,numero)
#     if opcion == 2:
#         listar_contactos(contactos)
#     if opcion == 3:
#         nombre = input("Nombre ")   
#         eliminar_contactos (nombre)
#     if opcion == 4:
#         id= int(input("Ingrese id a llamar "))
#         print("")
#         call_id(contactos,id)
#     print("")
#     gt = input("Desea realizar otra accion? ")
   
ChequeoArchivoExistenteConImpresion ()





