contactos=[{"nombre":"fabricio","apellido":"perez","numero":"44"},{"nombre":"andres","apellido":"alvarado","numero":"46"}]

def agregar_contacto(nombreNuevo,apellidoNuevo,numeroNuevo):
    new_contact= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}
    contactos.append(new_contact)
    print (contactos)

def listar_contactos(contactos):
    print("---------------------------")
    print("---------------------------")
    for k in (contactos):
        contador=0
        for i,n in k.items():
            contador = contador +1
            print("-{} es:  {}".format(i,n))
        print("---------------------------")
        print("---------------------------")
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

        

        

        
