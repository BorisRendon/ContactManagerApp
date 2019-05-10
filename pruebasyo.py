import os.path,time,sys



"""""fase 1"""
contactos=[]

def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)


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

gt= "si"
while gt =="si":
    opcion = int(input("seleccione opcion(1=agregar,2=listar,3=eliminar)     "))
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
        
    gt = input("otra accion?")



def contact_id (contactos):
    contador = 1   
    contactos_cid={} 
    for i in contactos:
        contactos_cid[contador]=i
        contador = contador +1
    print (contactos_cid)
    
contact_id(contactos)

id= int(input("ingrese ids a llamar separados por comas"))
def call_id (contactos,id):
    conta=contactos[id]
    id_per=conta ["nombre"]
    print ("calling {}... press c to cancel".format(id_per))
    contador =5
    for i in range(5):
        t0 = time.perf_counter()
        time.sleep(1)
        print("Espere en linea {} segundos restantes".format(contador))
        contador =contador - 1

call_id(contactos,id)
   






