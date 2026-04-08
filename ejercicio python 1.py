def agregar_cliente(lista_clientes, nombre):
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else:
        print("Debe agregar un nombre valido entre 2 y 50 caracteres.")

def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) or not (2 <= len(nuevo_nombre) <= 50):
        print("Nombre de cliente invalido, debe tener entre 2 y 50 caracteres")
        return
    if 0 <= indice < len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente modificado: {original} por -> {nuevo_nombre.title()}")
    else:
        print("No existe ese dato en la lista o indice incorrecto.")

def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice < len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("No se puede eliminar ese cliente, fuera del rango del indice")
def contar_clientes(lista_clientes):
    print(f"El total de clientes es: {len(lista_clientes)}")
def ordenar_clientes(lista_clientes):   
    for cliente in sorted(lista_clientes):
        print(cliente)

def main():
    clientes = ["ana", "carlos", "beatriz"]
    print("Clientes actuales")
    mostrar_clientes(clientes)
    agregar_cliente(clientes, "juan")
    mostrar_clientes(clientes)
    modificar_cliente(clientes, 1, "laura")
    mostrar_clientes(clientes)
    eliminar_cliente(clientes, 0)
    mostrar_clientes(clientes)
    contar_clientes(clientes)
    ordenar_clientes(clientes)

if __name__ == "__main__":
    main()