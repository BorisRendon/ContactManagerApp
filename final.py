contactos={1:{"nombre":"fabricio","apellido":"juarez","numero":"44"}}



def agregar_contacto(codigoUnico,nombreNuevo,apellidoNuevo,numeroNuevo):
    contactos[codigoUnico]= {"nombre":nombreNuevo,"apellido":apellidoNuevo,"numero":numeroNuevo}

def listar_contactos(contactos):
    for k in (contactos):
        print (k)
        for n,v in dict.keys(k):
            print (n)   
# agregar_contacto("2","fabricio","perez","65")
def eliminar_contactos (nombre):
    nombre_lista=list(nombre)
    nombre_cliente= nombre_lista[0]
    apellido_cliente = nombre lista[1]
        
# print(contactos)

# listar_contactos(contactos)

eliminar_contactos(fabricio perez)
    