import os.path,time,sys

"""""fase 1"""

contactos=[]
#fase 2


#---------------------------------------------------funcion traer .txt--------------------------------------------------------------
def agregar_txt(filename):

        with open(filename, 'r') as f:
                '''
                accion que realiza: agrega contactos de un archivo txt a la lista principal
                input: recibe el nombre del txt
                returns: nada '''
                for line in f.readlines():
                        lista = line.split(",")
                        
                        new_contact= {"nombre":lista[0],"apellido":lista[1],"numero":lista[2]}
                        contactos.append(new_contact)

#------------------------------------------------------funcion agregar contactos--------------------------------------------------
def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    '''
    accion que realiza: agrega un contacto a la lista
    input: recibe el nombre el apellido  y un # de telefono de 8 digitos
    returns: nada '''
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)
#------------------------------------------------------funcion listar contactos--------------------------------------------------
def listar_contactos(contactos):   
    '''
    accion que realiza: lista los contactos esteticamente
    input: recibe una lista de diccionarios como parametros
    returns: nada '''
    contador=0
    for k in (contactos):       
        print(" ---------------------------")
        print("|        contacto #{}       |".format(contador))
        print(" ---------------------------")
        for i,n in k.items(): 
            print("{}: {}".format(i,n))
        print ("contact id es {}".format(contador))
        contador = contador +1

#------------------------------------------------------funcion eliminar contactos--------------------------------------------------
def eliminar_contactos (contactos,nombre):
    '''
    accion que realiza: elimina los contactos
    input: recibe una lista de diccionarios y el nombre y apellido del contacto
    returns: nada '''
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
#------------------------------------------------------funcion chequeo de archivo con impresion--------------------------------------------------
"""Fase 2"""
listavacia = []
diccionario ={}
def ChequeoArchivoExistenteConImpresion ():
    '''
    accion que realiza: extrae contactos de un txt y los agrega a los contactos
    input: no recibe nada usa "initialContactList.txt"
    returns: nada '''
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
lista_conid = {}
def agregar_id(contactos):
        '''
        accion que realiza: agrega un id a los contactos
        input: recibe una lista de diccionarios como parametros
        returns: lista con id '''
        contador = 1
        for i in contactos:
                lista_conid[contador] = i
                contador = contador + 1
        print(lista_conid)
        return 
        lista_conid
def contact_id (contactos):
    '''
    ni idea de que hace '''
    contador = 0 
    contactos_cid={} 
    for i in contactos:
        contactos_cid[contador]=i
        contador = contador +1
#------------------------------------------------------funcion llamar contactos--------------------------------------------------
def call_id (contactos,id):
    '''
    accion que realiza: llama a contactos por id
    input: recibe una lista de diccionarios y el id a llamar
    returns: nada '''
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
#------------------------------------------------------funcion mensaje de textos ids--------------------------------------------------
def mensajes_ids(contactos,ids,mensaje):
        '''
        accion que realiza: envia mensaje a contacto por id
        input: recibe una lista de diccionarios, un id y un mensaje
        returns: nada '''
        id=contactos[ids]
        id_per=id["nombre"]
        id_num = id ["numero"]
        print ("enviando mensaje a: {} ({})".format(id_per,id_num))
        print ("mensaje: {}".format(mensaje))
        print("")
        print("enviando mensaje...")
        time.sleep(2)
#------------------------------------------------------funcion agregar a favoritos--------------------------------------------------
lista_favoritos=[]
def agregar_a_favo(contactos,ids):
        '''
        accion que realiza: agrega contactos a lista de favoritos
        input: recibe una lista de diccionarios, y un id
        returns: nada '''
        nuevo = contactos[ids]
        lista_favoritos.append(nuevo)
        return
        lista_favoritos
#------------------------------------------------------funcion listar contactos favoritos--------------------------------------------------
def listar_contactos_favoritos(lista_favoritos):   
    '''
    accion que realiza: lista los contactos esteticamente
    input: recibe una lista de diccionarios como parametros
    returns: nada '''
    contador=0
    for k in (lista_favoritos):       
        print(" ---------------------------")
        print("| contacto favorito #{}     |".format(contador))
        print(" ---------------------------")
        for i,n in k.items(): 
            print("{}: {}".format(i,n))
        print ("contact id de favoritos es {}".format(contador))
        contador = contador +1
opciones_principal = [1,2,3,4,10]
#------------------------------------------------------menu-----------------------------------------------------------
agregar_txt("ejemplo.txt")
menup = "si"
while menup == "si":
        print("")
        print("--------------------------------menu principal contact manager--------------------------------------------")
        print("")
        print("1. ajustes de contactos")
        print("2. comunicarse con algun contacto")
        print("3. favoritos")
        print("4. HELP")
        print("10. exit ")
        print("")
        opcion_menu_prin = input("ingrese numero de opcion: ")
        if opcion_menu_prin == "1" :               
                menuaj = "si"
                while menuaj =="si":
                        print("")
                        print("-----------------------------------Ajustes de contactos----------------------------------------")
                        print("")
                        print("1. agregar contactos")
                        print("2. listar contactos")
                        print("3. eliminar contactos")
                        print("4. agrgar txt")
                        print("10. exit ajustes de contacto")
                        print("")
                        opcion_ajustes = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_ajustes == "1":
                                nombre = input("Nombre:  ")
                                apellido = input("Apellido: ")
                                numero =int(input("Numero (8 digitos): "))
                                if numero<9999999 or numero>99999999:
                                        numero =input("ingrese numero valido (se cancelara operacion si no lo hace): ")
                                agregar_contacto(nombre,apellido,numero)
                                print("contacto agregado")
                                time.sleep(1)
                        if opcion_ajustes == "2":
                                listar_contactos(contactos)
                        if opcion_ajustes == "3":
                                nombre = input("Nombre y apellido: ")   
                                eliminar_contactos (contactos,nombre)
                        if opcion_ajustes == "4":
                                filename = input("ingrese nombre de archivo: ")
                                agregar_txt(filename)   
                        if opcion_ajustes == "10":
                                menuaj= "salir"
        if opcion_menu_prin == "2" :
                menucont = "si"
                while menucont == "si":
                        print("")
                        print("----------------------------------comunicarse con contactos-----------------------------------------------")
                        print("")
                        print("1. llamar contacto ")
                        print("2. mensaje a contacto")
                        print("3. agregar contacto a favorito")
                        print("4. listar contactos favoritos")
                        print("5. llamar contacto de favoritos")
                        print("6. mensaje a contacto de favoritos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_cont = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_cont == "1":
                                id= int(input("Ingrese id a llamar: "))
                                print("")
                                call_id(contactos,id)
                                print("")
                        if opcion_cont == "2":
                                ids= int(input("Ingrese id a mandar mensaje: "))
                                mensaje = input("ingrese mensaje: ")
                                mensajes_ids(contactos,ids,mensaje)                               
                                print("")
                        if opcion_cont == "3":
                                ids = int(input("ingrese id para agregar a favoritos: "))
                                agregar_a_favo(contactos,ids)
                                print("")
                                print("contacto agregado")
                                time.sleep(1)
                             
                        if opcion_cont == "10":
                                menucont= "exit"
        if opcion_menu_prin == "3" :
                menufav = "si"
                while menufav == "si":
                        print("")
                        print("--------------------------------Favoritos-----------------------------------------------")
                        print("")
                        print("1. agregar contacto a favorito")
                        print("2. listar contactos favoritos")
                        print("3. eliminar contacto de favoritos")
                        print("4. llamar contacto de favoritos")
                        print("4. mensaje a contacto de favoritos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_help = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_help == "1":
                                ids = int(input("ingrese id para agregar a favoritos: "))
                                agregar_a_favo(contactos,ids)
                                print("")
                                print("contacto agregado")
                                time.sleep(1)
                        if opcion_help == "2":
                                print("")
                                listar_contactos_favoritos(lista_favoritos)
                        if opcion_help == "4":
                                id= int(input("Ingrese id de favorito a llamar: "))
                                print("")
                                call_id(lista_favoritos,id)
                                print("")
                        if opcion_help == "5":
                                ids= int(input("Ingrese id de favorito a mandar mensaje: "))
                                mensaje = input("ingrese mensaje: ")
                                mensajes_ids(lista_favoritos,ids,mensaje)                               
                                print("")  
                        if opcion_help == "3":
                                nombre = input("Nombre y apellido: ")   
                                eliminar_contactos (lista_favoritos,nombre)     
                        if opcion_help == "10":
                                menufav= "exit" 
        if opcion_menu_prin == "4" :
                menu_help = "si"
                while menu_help == "si":
                        print("")
                        print("----------------------------------HELP--------------------------------------------")
                        print("")
                        print("1. agregar archivo de contactos")
                        print("2. agregar contactos")
                        print("3. listar contactos")
                        print("4. llamar contacto de favoritos")
                        print("4. mensaje a contacto de favoritos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_help = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_help == "1":
                                print(agregar_txt.__doc__)
                                print("")
                                time.sleep(1)
                        if opcion_help == "2":
                                print(agregar_contacto.__doc__)
                                print("")
                        if opcion_help == "3":
                                print(listar_contactos.__doc__)
                                print("")
                        if opcion_help == "5":
                                ids= int(input("Ingrese id de favorito a mandar mensaje: "))
                                mensaje = input("ingrese mensaje: ")
                                mensajes_ids(lista_favoritos,ids,mensaje)                               
                                print("")  
                        if opcion_help == "3":
                                nombre = input("Nombre y apellido: ")   
                                eliminar_contactos (lista_favoritos,nombre)     
                        if opcion_help == "10":
                                menu_help= "exit"                                       
        if opcion_menu_prin == "10" :
                print("cerrando contact manager")
                time.sleep(2)
                sys.exit(0)