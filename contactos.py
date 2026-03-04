agenda = []

def agregar_contacto(nombre, telefono):
    agenda.append({"nombre": nombre, "telefono": telefono})
    
def listar_contactos():
    return agenda