# vamos a creqar un inventareio pero utilizar nombre y precio 
"""
.append() agregar
.insert ()
remove() / pop()
.sort()  ordenar
invertir() invertir los valores
"""

def mostrar_inventario(productos):
        print("mostrar inventario")
        if not productos:
            print("No hay productos registrados")
            return
        for i, producto in enumerate (productos, start=1):
                print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto(productos, nombre, precio):
        if isinstance(nombre,str) and nombre.strip() and isinstance(precio, (int, float)) and precio > 0:
            productos.append({"nombre":nombre.tittle(), "precio":precio})
            print(f"producto'{nombre.tittle()}' agregado.")

        else:
              print("Producto no agregado, datos invalidos, el valor debe ser un numero positivo")

if __name__=="__main__":
    inventario=[
        {"nombre": "Taladro", "precio":150000},
        {"nombre": "Martillo", "precio":40000},
        {"nombre": "Destornillador", "precio":15000}
    ]

    mostrar_inventario(inventario)

    #Agregar inventario
    agregar_producto (inventario, "Sierra Circular", 220000)
    mostrar_inventario (inventario)
