def agregar_txt(filename):
        with open(filename, 'r') as f:
                for line in f.readlines():
                        lista = line.split(",")
                        
                        new_contact= {"nombre":lista[0],"apellido":lista[1],"numero":lista[2]}
                        contactos.append(new_contact)