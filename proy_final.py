import requests
import os.path,time,sys,requests
contactos=[]
def get_contacts (url):
        r = requests.get(url = url)
        data = r.json()
        for i in data:
                contactos.append(i)


#---------------------------------------------------funcion traer .txt--------------------------------------------------------------
def agregar_txt (path,documento):
        '''
        accion que realiza: agrega un txt desde la computadora
        input: path de la carpeta y el nombre del archivo
        returns: nada '''
        if os.path.isdir:
                directory = os.path.normpath(path)
                for subdir, dirs, files in os.walk(directory):
                        for file in files:
                                if file.endswith(documento):
                                        with open(os.path.join(subdir, file),'r') as f:
                                                for line in f.readlines():
                                                                        
                                                        try:

                                                                lista = line.split(",")
                                                                
                                                                new_contact= {"FirstName":lista[0],"LastName":lista[1],"Phone":lista[2]}
                                                                contactos.append(new_contact)
                                                        except:
                                                                IndexError 
                                                                print("")
                                                                print ("[ERROR] al agregar la linea")
        else:
                print("directorio no existe")
agregar_txt("C:/Users/fabri/Documents/GitHub/ContactManagerApp","ejemplo.txt")     

#------------------------------------------------------funcion agregar contactos--------------------------------------------------
def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    '''
    accion que realiza: agrega un contacto a la lista
    input: recibe el nombre el apellido  y un # de telefono de 8 digitos
    returns: nada '''
    new_contact= {"FirstName":nombreNuevo,"LastName":apellidoNuevo,"Phone":numeroNuevo}
    contactos.append(new_contact)
#------------------------------------------------------funcion listar contactos--------------------------------------------------
def listar_contactos(contactos):

        '''
        accion que realiza: lista los contactos esteticamente
        input: recibe una lista de diccionarios como parametros
        returns: nada '''
        try:

                contador=0
                for k in (contactos):       
                        print(" ---------------------------")
                        print("|        contacto #{}       |".format(contador))
                        print(" ---------------------------")
                        for i,n in k.items(): 
                                print("{}: {}".format(i,n))
                        print ("contact id es {}".format(contador))
                        contador = contador +1
                        print("")
                print("press crtl+c to exit")
                time.sleep(444444)
        except:
                KeyboardInterrupt
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
        if i["FirstName"]==nombre_cliente:
            if i["LastName"] == apellido_cliente:
                eliminar = contactos[conta]
                contactos.remove(eliminar)
                
        conta = conta +1    
#------------------------------------------------------funcion llamar contactos--------------------------------------------------
def call_id (contactos,id):
        '''
        accion que realiza: llama a contactos por id
        input: recibe una lista de diccionarios y el id a llamar
        returns: nada '''
        conta=contactos[id]
        id_per=conta ["FirstName"]
        id_num = conta ["Phone"]
        print ("calling {}...".format(id_per))
        print("numero de telefono: {}".format(id_num))
        contador =5
        try:
                for i in range(5):
                        time.sleep(1)
                        print("Espere en linea {} segundos restantes".format(contador))
                        contador =contador - 1
        except:
                KeyboardInterrupt
#------------------------------------------------------funcion mensaje de textos ids--------------------------------------------------
def mensajes_ids(contactos,ids,mensaje):
        '''
        accion que realiza: envia mensaje a contacto por id
        input: recibe una lista de diccionarios, un id y un mensaje
        returns: nada '''
        id=contactos[ids]
        id_per=id["FirstName"]
        id_num = id ["Phone"]
        print ("enviando mensaje a: {} {}".format(id_per,id_num))
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
        try:

                contador=0
                for k in (lista_favoritos):       
                        print(" ---------------------------")
                        print("| contacto favorito #{}     |".format(contador))
                        print(" ---------------------------")
                        for i,n in k.items(): 
                                print("{}: {}".format(i,n))           
                        print ("contact id de favoritos es {}".format(contador))
                        contador = contador +1
                        print("")
                print("press ctrl+c to exit")
                time.sleep(444444)
        except:
                KeyboardInterrupt
        

#------------------------------------------------------menu-----------------------------------------------------------

menup = "si"
while menup == "si":
        os.system('cls')
        print("")
        print("--------------------------------menu principal contact manager--------------------------------------------")
        print("")
        print("1. Ajustes de contactos")
        print("2. Comunicarse con algun contacto")
        print("3. Favoritos")
        print("4. Get-Post")
        print("5. Help")
        print("10. exit ")
        print("")
        opcion_menu_prin = input("ingrese numero de opcion: ")
        if opcion_menu_prin == "1" :               
                menuaj = "si"
                while menuaj =="si":
                        os.system('cls')
                        print("")
                        print("-----------------------------------Ajustes de contactos--------------------------------------")
                        print("")
                        print("1. agregar contactos")
                        print("2. listar contactos")
                        print("3. eliminar contactos")
                        print("4. agregar txt")
                        print("10. exit ajustes de contacto")
                        print("")
                        opcion_ajustes = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_ajustes == "1":
                                nombre = input("Nombre:  ")
                                apellido = input("Apellido: ")
                                numero =int(input("Numero: "))
                                largonumero = len(numero)
                                
                                agregar_contacto(nombre,apellido,numero)
                                print("contacto agregado")
                                time.sleep(1)
                        if opcion_ajustes == "2":
                                listar_contactos(contactos)
                        if opcion_ajustes == "3":
                                nombre = input("Nombre y apellido: ")   
                                eliminar_contactos (contactos,nombre)
                        if opcion_ajustes == "4":
                                path = input("ingrese path de archivo: ")
                                documento = input("ingrese nombre de archivo: ")
                                agregar_txt(path,documento)   
                        if opcion_ajustes == "10":
                                menuaj= "salir"
        if opcion_menu_prin == "2" :
                menucont = "si"
                while menucont == "si":
                        os.system('cls')
                        print("")
                        print("----------------------------------comunicarse con contactos-----------------------------------------------")
                        print("")
                        print("1. llamar contacto ")
                        print("2. mensaje a contacto")
                        print("3. listar contactos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_cont = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_cont == "1":
                                id= int(input("Ingrese id a llamar: "))
                                if id<len(contactos):
                                        print("")
                                        call_id(contactos,id)
                                        print("")
                                else:
                                        print("")
                                        print("id no existe")
                                        time.sleep(2)
                        if opcion_cont == "2":
                                ids= int(input("Ingrese id a mandar mensaje: "))
                                if ids< len(contactos):
                                        mensaje = input("ingrese mensaje: ")
                                        mensajes_ids(contactos,ids,mensaje)                               
                                        print("")
                                else:
                                        print("")
                                        print("id no existe")
                                        time.sleep(2)
                        if opcion_cont == "3":
                                listar_contactos(contactos)
                             
                        if opcion_cont == "10":
                                menucont= "exit"
        if opcion_menu_prin == "3" :
                menufav = "si"
                while menufav == "si":
                        os.system('cls')
                        print("")
                        print("--------------------------------Favoritos-----------------------------------------------")
                        print("")
                        print("1. agregar contacto a favorito")
                        print("2. listar contactos favoritos")
                        print("3. eliminar contacto de favoritos")
                        print("4. llamar contacto de favoritos")
                        print("5. mensaje a contacto de favoritos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_help = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_help == "1":
                                ids = int(input("ingrese id para agregar a favoritos: "))
                                if ids < len(contactos):
                                        agregar_a_favo(contactos,ids)
                                        print("")
                                        print("contacto agregado")
                                        time.sleep(1)
                                else:
                                        print("")
                                        print("id no existe")
                                        time.sleep(2)
                        if opcion_help == "2":
                                print("")
                                listar_contactos_favoritos(lista_favoritos)
                        if opcion_help == "4":
                                id= int(input("Ingrese id de favorito a llamar: "))
                                if id < len(lista_favoritos):
                                        print("")
                                        call_id(lista_favoritos,id)
                                        print("")
                                else:
                                        print("")
                                        print("id no existe")
                                        time.sleep(2)
                        if opcion_help == "5":
                                ids= int(input("Ingrese id de favorito a mandar mensaje: "))
                                if ids < len(lista_favoritos):
                                        mensaje = input("ingrese mensaje: ")
                                        mensajes_ids(lista_favoritos,ids,mensaje)                               
                                        print("")  
                                else:
                                        print("")
                                        print("id no existe")
                                        time.sleep(2)
                        if opcion_help == "3":
                                nombre = input("Nombre y apellido: ")   
                                eliminar_contactos (lista_favoritos,nombre)     
                        if opcion_help == "10":
                                menufav= "exit" 
        if opcion_menu_prin == "5" :
                menu_help = "si"
                while menu_help == "si":
                        os.system('cls')
                        print("")
                        print("----------------------------------HELP--------------------------------------------")
                        print("")
                        print("1. agregar archivo de contactos")
                        print("2. agregar contactos")
                        print("3. listar contactos")
                        print("4. eliminar contactos")
                        print("5. llamar a contacto")
                        print("6. mensaje a contacto")
                        print("7. agregar contacto a favoritos")
                        print("10. exit comunicarse con algun contacto")
                        print("")
                        opcion_help = input("ingrese numero de opcion: ")
                        print("")
                        if opcion_help == "1":
                                print(agregar_txt.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "2":
                                print(agregar_contacto.__doc__)
                                time.sleep(3)
                                print("")
                        if opcion_help == "3":
                                print(listar_contactos.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "4":
                                print(eliminar_contactos.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "5":
                                print(call_id.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "6":
                                print(mensajes_ids.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "7":
                                print(agregar_a_favo.__doc__)
                                print("")
                                time.sleep(3)
                        if opcion_help == "8":
                                print(listar_contactos_favoritos.__doc__)
                                print("")
                                time.sleep(3)   
                        if opcion_help == "10":
                                menu_help= "exit"                                       
        if opcion_menu_prin == "4":
                menupg = "si"
                while menupg =="si":
                        print("")
                        print("-----------------------------------Get-Post--------------------------------------")
                        print("")
                        print("1. get contacts")
                        print("2. post contacts")
                        print("10. exit ajustes de contacto")
                        print("")
                        opcionpg = input("ingrese numero de opcion: ")
                        print("")
                        if opcionpg == "1":
                                url = input("ingrese url para traer datos: ")
                                get_contacts(url)
                        if opcionpg == "2":
                                data = contactos
                                r = requests.post("http://demo7862839.mockable.io/contacts?gid=100", json={'json_payload': data})  
                        if opcionpg == "10":
                                menupg = "exit"


        if opcion_menu_prin == "10" :
                os.system('cls')
                print("cerrando contact manager")
                time.sleep(2)
                sys.exit()
